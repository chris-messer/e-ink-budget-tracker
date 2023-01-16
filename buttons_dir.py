from gpiozero import Button
from services.print_budget import refresh_budget
from utils.print_to_eink import print_text
from utils.build_images import plain_text
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

def key1():
    refresh_budget(monthly_budget, _debug=False)

def key2():
    print_text(Image.open('images/piggy.bmp'))

def key3():
    print_text(plain_text("Key 3 Pressed"))

def key4():
    print_text(plain_text("Key 4 Pressed"))


btn1.when_pressed = key1
btn2.when_pressed = key2
btn3.when_pressed = key3
btn4.when_pressed = key4

