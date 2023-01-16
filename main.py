import os
import dotenv
from get_balance_info import Bank, weekly_budget_remaining
from dotenv import load_dotenv
from _display import build_image
from print_to_eink import print_text
import pickle

username = os.getenv('username')
password = os.getenv('password')

monthly_budget = 5000

load_dotenv()

while True:
    bank = Bank(username, password)
    budget_dict = weekly_budget_remaining(bank,
                                          '75417769_13615882',
                                          monthly_budget)
    pickle.dump(budget_dict, open("budget.p","wb"))

    # budget_dict = pickle.load(open("budget.p", "rb"))
    img = build_image(budget_dict)
    print_text(img)

    print('pause')