from services.print_budget import refresh_budget
import time
from dotenv import load_dotenv
import logging
import os

logging.basicConfig(level=logging.INFO)
load_dotenv()

monthly_budget = os.getenv('monthly_budget')

while True:
    refresh_budget(monthly_budget, _debug=True)
    time.sleep(10000)
    print('pause')