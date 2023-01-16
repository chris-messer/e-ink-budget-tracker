from dotenv import load_dotenv
import logging
import os
from utils.get_balance_info import Bank, weekly_budget_remaining
from utils.build_images import plain_text, build_budget_text
import pickle
try:
    from utils.print_to_eink import print_text
except:
    pass

logging.basicConfig(level=logging.INFO)
load_dotenv()

def refresh_budget(monthly_budget, _debug):
    username = os.getenv('username')
    password = os.getenv('password')

    logging.info("Connecting to Mint")
    print_text(plain_text('Refreshing Budget...'))

    if _debug == True:
        budget_dict = pickle.load(open("../budget.p", "rb"))
    else:
        bank = Bank(username, password)
        budget_dict = weekly_budget_remaining(bank,
                                              '75417769_13615882',
                                              monthly_budget)
        pickle.dump(budget_dict, open("./budget.p", "wb"))


    logging.info("Building Image")

    budget_text = build_budget_text(budget_dict)
    img = plain_text(budget_text)

    logging.info("Printing Image")
    print_text(img)