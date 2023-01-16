from services.print_budget import refresh_budget, refresh_screen
import time
from dotenv import load_dotenv
import logging
import os
import threading

logging.basicConfig(level=logging.INFO)
load_dotenv()

monthly_budget = int(os.getenv('monthly_budget'))

def refresh_budget_thread(monthly_budget, _debug=False):
    refresh_budget(monthly_budget, _debug=False)
    time.sleep(1800)

def refresh_screen_thread():
    refresh_screen()
    time.sleep(175)

while True:

    api_pull=threading.Thread(target=refresh_budget,
                              args=(monthly_budget, _debug=False))
    screen_refresh=threading.Thread(target=refresh_screen_thread)

    api_pull.start()
    time.sleep(180)
    screen_refresh.start()


    print('pause')