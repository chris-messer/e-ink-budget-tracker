from gpiozero import Button
from main import refresh_budget
from PIL import Image, ImageDraw, ImageFont
from print_to_eink import print_text
from print_to_eink import print_text

btn1 = Button(5)
btn2 = Button(6)
btn3 = Button(13)
btn4 = Button(19)

def handleBtnPress(btn):
    pinNum = btn.pin.number
    switcher = {
        5: refresh_budget(),
        6: print_text(Image.open('images/piggy.bmp')),
        13: "Hope you lik it.",
        19: "Goodbye!"
    }
    msg = switcher.get(pinNum, "Error")

btn1.when_pressed = handleBtnPress
btn2.when_pressed = handleBtnPress
btn3.when_pressed = handleBtnPress
btn4.when_pressed = handleBtnPress

