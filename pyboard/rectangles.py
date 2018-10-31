import lcd160cr
import pyb

lcd = lcd160cr.LCD160CR('X')

fg = lcd.rgb(0,0,0)
bg = lcd.rgb(255, 255, 255)
lcd.set_pen(fg, bg)

padding = 10
w = 40
h = 30

def draw_buttons():
    # top left
    lcd.rect(padding, padding, w, h)

    # top right
    lcd.rect(lcd.w - w - padding, padding, w, h)

    # bottom left
    lcd.rect(padding, lcd.h - h - padding, w, h)

    # bottom right
    lcd.rect(lcd.w - w - padding, lcd.h - h - padding, w, h)

def draw_message_box():
    x = int((lcd.w / 2) - (w / 2))
    y = int((lcd.h / 2) - (h / 2))
    lcd.rect(x, y, w, h)

def handle_touch():
    touched, touch_x, touch_y = lcd.get_touch()
    message = [str(touch_x), str(touch_y)]
    if touch_x < padding + w:
        message.append("left")
    elif lcd.w - padding - w < touch_x:
        message.append("right")
    else:
        message.append("middle")

    x = int(lcd.w / 2)
    y = int(lcd.h / 2)
    lcd.set_pos(x, y)
    lcd.set_text_color(fg, bg)
    lcd.write(" ".join(message))


def get_message():
    touched, touch_x, touch_y = lcd.get_touch()
    message = []

    if touch_y < padding + h:
        message.append("top")
    elif lcd.h - padding - h < touch_y:
        message.append("bottom")

    if touch_x < padding + w:
        message.append("left")
    elif lcd.w - padding - w < touch_x:
        message.append("right")

    return message

def write_message(message):
    x = int(lcd.w / 2)
    y = int(lcd.h / 2)
    lcd.set_pos(x, y)
    lcd.set_text_color(fg, bg)
    lcd.write(" ".join(message))

def handle_button_click():
    message = get_message()
    if len(message) == 2:
        write_message(" ".join(message))
    else:
        write_message("miss")

def loop():
    starting_touch = lcd.get_touch()
    while lcd.get_touch() == starting_touch:
        pyb.delay(100)
    lcd.erase()
    draw_buttons()
    handle_button_click()
    loop()

def main():
    lcd.erase()
    draw_buttons()
    loop()
