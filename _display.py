from PIL import Image, ImageDraw, ImageFont

def build_image(budget_dict):
    # create an image
    out = Image.new("RGB", (264, 176), (255, 255, 255))

    # get a font
    fnt = ImageFont.truetype("fonts/arial.ttf", 18)
    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw multiline text

    wbr = round(budget_dict['remaining_weekly_budget'],2)
    cur_bal = round(budget_dict['current_balance'], 2)

    _text = f"Weekly Remaining:   ${wbr}\n\n" \
            f"Current Balance:        ${cur_bal}"
    d.multiline_text((10, 10), _text, font=fnt, fill=(0, 0, 0))

    out.show()