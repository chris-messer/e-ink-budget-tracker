from services.print_budget import refresh_budget, refresh_screen
import time
from dotenv import load_dotenv
import logging
import os
import threading
import buttons_dir

logging.basicConfig(level=logging.INFO)
load_dotenv()

monthly_budget = int(os.getenv('monthly_budget'))

def refresh_budget_thread(monthly_budget, _debug=False):
    while True:
        refresh_budget(monthly_budget, _debug=False)
        time.sleep(1800)

def refresh_screen_thread():
    while True:
        time.sleep(175)
        refresh_screen()




api_pull=threading.Thread(target=refresh_budget,
                          args=(monthly_budget, False))
screen_refresh=threading.Thread(target=refresh_screen_thread)

button_listen=threading.Thread(target=buttons_dir.button_listen)

api_pull.start()
button_listen.start()

screen_refresh.start()


print('pause')