import os
import dotenv
from get_balance_info import Bank, weekly_budget_remaining
from dotenv import load_dotenv
from _display import plain_text, build_budget_text
import pickle
import logging
import time

try:
    from print_to_eink import print_text
except:
    pass


logging.basicConfig(level=logging.INFO)

username = os.getenv('username')
password = os.getenv('password')

monthly_budget = 5000

load_dotenv()

def refresh_budget():
    logging.info("Connecting to Mint")
    print_text(plain_text('Refreshing Balance...'))
    bank = Bank(username, password)
    budget_dict = weekly_budget_remaining(bank,
                                          '75417769_13615882',
                                          monthly_budget)
    pickle.dump(budget_dict, open("budget.p", "wb"))

    # budget_dict = pickle.load(open("budget.p", "rb"))
    logging.info("Building Image")

    budget_text = build_budget_text(budget_dict)
    img = plain_text(budget_text)

    logging.info("Printing Image")
    print_text(img)


while True:
    refresh_budget()
    time.sleep(10000)
    print('pause')