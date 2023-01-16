import os
import dotenv
from get_balance_info import Bank, weekly_budget_remaining
from dotenv import load_dotenv
from _display import build_image
from print_to_eink import print_text
import pickle
import logging

logging.basicConfig(level=logging.INFO)

username = os.getenv('username')
password = os.getenv('password')

monthly_budget = 5000

load_dotenv()

while True:
    logging.info("Connecting to Mint")
    bank = Bank(username, password)
    budget_dict = weekly_budget_remaining(bank,
                                          '75417769_13615882',
                                          monthly_budget)
    pickle.dump(budget_dict, open("budget.p","wb"))

    # budget_dict = pickle.load(open("budget.p", "rb"))
    logging.info("Building Image")
    img = build_image(budget_dict)

    logging.info("Printing Image")
    print_text(img)

    print('pause')