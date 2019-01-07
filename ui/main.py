import m5stack

tft = m5stack.Display()

AVAILABLE_NUM_WORDS = [12, 15, 18, 21, 24]
AVAILABLE_STEPS = [
    'choose mnemonic words number',
    'generate mnemonic',
    'guess the 5th word',
    'display menu',
    'continue'
]

AVAILABLE_MNEMONICS = {
    '12': 'together strong topple gown hospital people pig spend sport sweet choose solve',
    '18': 'when pool song man agree when hair ring undo weapon art number phone recycle journey drill word inherit',
    '24': 'tonight slim actress bargain wrestle debris warfare flight switch hero forget flip exercise put retire screen organ wisdom sick banner bench mask key identify',
}

active_step = 0
num_words_index = 0

# print functions

def print_title(text):
    tft.text(tft.CENTER, 20, text)

def print_line_1(text):
    tft.text(tft.CENTER, 50, text)

def print_line_2(text):
    tft.text(tft.CENTER, 70, text)

def print_line_3(text):
    tft.text(tft.CENTER, 90, text)

def print_button_a(text):
    tft.text(40, 208, text)

def print_button_b(text):
    tft.text(tft.CENTER, 208, text)

def print_button_c(text):
    tft.text(235, 208, text)


def button_handler_a(pin, pressed):
    # if button was released
    if pressed is False:
        next_step()
        print("Button A pressed")

def button_handler_b(pin, pressed):
    # if button was released
    if pressed is False:
        next_step()
        print("Button B pressed")

def button_handler_c(pin, pressed):
    # if button waas released
    if pressed is False:
        next_step()
        print("Button C pressed")

def next_step():
    global active_step
    active_step += 1
    print(active_step)

# set the buttons events
m5stack.ButtonA(callback=button_handler_a)
m5stack.ButtonB(callback=button_handler_b)
m5stack.ButtonC(callback=button_handler_c)


def select_entropy():
    print_line_1("Choose mnemonic words")
    print_button_a('12 words')
    print_button_b('18 words')
    print_button_c('24 words')


def clean_screen():
    clear = '               '
    print_line_1(clear)
    print_line_2(clear)
    print_line_3(clear)
    print_button_a(clear)
    print_button_b(clear)
    print_button_c(clear)


def main():
    print_title("Welcome to the buidl wallet!")

    # choose the entropy
    num_words = select_entropy()

    # generate the mnemonic (entropy)

    # guess the 5th word

    # display menu

    # user cli.py to sign a transtion


if __name__ == '__main__':
    main()
