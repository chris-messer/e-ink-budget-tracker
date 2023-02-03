from services.print_budget import refresh_budget, refresh_screen
import time
from dotenv import load_dotenv
import logging
import os
import threading


logging.basicConfig(level=logging.INFO)
load_dotenv()

monthly_budget = int(os.getenv('monthly_budget'))
refresh_budget(monthly_budget, _debug=False)
