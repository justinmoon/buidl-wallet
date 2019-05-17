import urandom
import m5stack
import time
import tcc
import machine

tft = m5stack.Display()


DEMO_MNEMONIC = ['tonight', 'slim', 'actress', 'bargain', 'wrestle', 'debris', 'warfare', 'flight', 'switch', 'hero', 'forget', 'flip', 'exercise', 'put', 'retire', 'screen', 'organ', 'wisdom', 'sick', 'banner', 'bench', 'mask', 'key', 'identify']

mnemonic = ''
lock = True

# Wallet generation
GENERATE_MNEMONIC_STEP = 0
SHOW_MNEMONIC_STEP = 1
GUESS_WORD_STEP = 2
DISPLAY_MENU_STEP = 4
END_STEP = 4

active_step = GENERATE_MNEMONIC_STEP

################
# Wallet Stuff #
################


def entropy(n: int):
    # TODO: hardware RNG
    return bytes([urandom.getrandbits(8) for _ in range(n)])

def init():
    data = entropy(32)
    print("bip39 entropy=", data)
    mnemonic = tcc.bip39.from_data(data)
    print("mnemonic=", mnemonic)
    return mnemonic

def display_title(text):
    tft.text(tft.CENTER, 20, text)

def display_content(lines):
    for i, line in enumerate(lines):
        height = 50 + 20 * i
        # TODO: assert on length
        tft.text(5, height, line)

def display_buttons(a, b, c):
    tft.text(40, 208, a)
    tft.text(tft.CENTER, 208, b)
    tft.text(235, 208, c)

def unlock():
    global lock
    lock = False
    print('unlocking')

def set_mnemonic(val):
    global mnemonic
    mnemonic = val

def button_handler_a(pin, pressed):
    # if button was pressed
    if pressed is True:
        if active_step == GENERATE_MNEMONIC_STEP:
            print(1)
            set_mnemonic(init())
            print(2)
            unlock()

        print("Button A pressed")


def button_handler_b(pin, pressed):
    # if button was released
    if pressed is True:
        if active_step == GENERATE_MNEMONIC_STEP:
            set_mnemonic(DEMO_MNEMONIC[:18])
            unlock()

        print("Button B pressed")

def button_handler_c(pin, pressed):
    # if button was released
    if pressed is True:
        if active_step == GENERATE_MNEMONIC_STEP:
            set_mnemonic(DEMO_MNEMONIC)
            unlock()
        elif active_step == SHOW_MNEMONIC_STEP:
            unlock()

        print("Button C pressed")

# set the buttons events
m5stack.ButtonA(callback=button_handler_a)
m5stack.ButtonB(callback=button_handler_b)
m5stack.ButtonC(callback=button_handler_c)


def generate_mnemonic():
    # clean_screen()
    tft.clear()

    display_title("Choose mnemonic length")
    display_buttons('12 words', '18 words', '24 words')

def show_mnemonic():
    tft.clear()
    display_title("Write down your mnemonic:")

    # 4 words at a time
    # TODO: print columns, number words
    # contents = [' '.join(mnemonic[4*i:4*i+4]) for i in range(6) ]
    contents = mnemonic.split()
    display_content(contents)

    display_buttons('', '', 'Done')

def save():
    pass

def menu():
    pass

def guess_word():
    tft.clear()
    display_content(["WORK IN PROGRESS"])

def main():
    global active_step

    available_steps = {
        GENERATE_MNEMONIC_STEP: generate_mnemonic,
        SHOW_MNEMONIC_STEP: show_mnemonic,
        GUESS_WORD_STEP: guess_word,
        DISPLAY_MENU_STEP: menu,
        END_STEP: save
    }

    global lock

    while True:
        lock = True
        available_steps[active_step]()

        while lock:
            time.sleep_ms(100)

        # after unlock go to next step
        active_step += 1
        print("active step: ", active_step)

if __name__ == '__main__':
    display_title("Welcome to the buidl wallet!")
    # main()
