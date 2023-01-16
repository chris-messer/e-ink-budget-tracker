from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import logging
import os


logging.basicConfig(level=logging.INFO)
load_dotenv()


def plain_text(_text):
    out = Image.new("RGB", (264, 176), (255, 255, 255))
    fnt = ImageFont.truetype("fonts/arial.ttf", 18)
    d = ImageDraw.Draw(out)

    d.multiline_text((10, 10), _text, font=fnt, fill=(0, 0, 0))

    # out.show()
    return out

def build_budget_text(budget_dict):
    wbr = round(budget_dict['remaining_weekly_budget'], 2)
    cur_bal = round(budget_dict['current_balance'], 2)

    _text = f"Weekly Remaining:   ${wbr}\n\n" \
            f"Current Balance:        ${cur_bal}"
    return _text

