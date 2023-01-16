from gpiozero import Button
from services.print_budget import refresh_budget
from utils.print_to_eink import print_text
from PIL import Image
from dotenv import load_dotenv
import logging
import os


logging.basicConfig(level=logging.INFO)
load_dotenv()

btn1 = Button(5)
btn2 = Button(6)
btn3 = Button(13)
btn4 = Button(19)
monthly_budget = os.getenv('monthly_budget')

def handleBtnPress(btn):
    pinNum = btn.pin.number
    switcher = {
        5: refresh_budget(monthly_budget, _debug=False),
        6: print_text(Image.open('images/piggy.bmp')),
        13: "Hope you lik it.",
        19: "Goodbye!"
    }
    msg = switcher.get(pinNum, "Error")

btn1.when_pressed = handleBtnPress
btn2.when_pressed = handleBtnPress
btn3.when_pressed = handleBtnPress
btn4.when_pressed = handleBtnPress

