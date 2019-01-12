import m5stack
import time

tft = m5stack.Display()

GENERATE_MNEMONIC_STEP = 0
SHOW_MNEMONIC_STEP = 1
GUESS_WORD_STEP = 2
DISPLAY_MENU_STEP = 4
END_STEP = 4

AVAILABLE_MNEMONICS = {
    '12': 'together strong topple gown hospital people pig spend sport sweet choose solve',
    '18': 'when pool song man agree when hair ring undo weapon art number phone recycle journey drill word inherit',
    '24': 'tonight slim actress bargain wrestle debris warfare flight switch hero forget flip exercise put retire screen organ wisdom sick banner bench mask key identify',
}

mnemonic = ''
lock = True

# starts on step 0
active_step = GENERATE_MNEMONIC_STEP

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

def unlock():
    global lock
    lock = False
    print('unlocking')
    print(lock)

def set_mnemonic(val):
    global mnemonic
    mnemonic = val

def button_handler_a(pin, pressed):
    # if button was pressed
    if pressed is True:
        if active_step == GENERATE_MNEMONIC_STEP:
            set_mnemonic(AVAILABLE_MNEMONICS['12'])
            unlock()
        elif active_step == SHOW_MNEMONIC_STEP:
            unlock()

        print("Button A pressed")


def button_handler_b(pin, pressed):
    # if button was released
    if pressed is False:
        if active_step == GENERATE_MNEMONIC_STEP:
            set_mnemonic(AVAILABLE_MNEMONICS['18'])
            unlock()


        print("Button B pressed")

def button_handler_c(pin, pressed):
    # if button was released
    if pressed is False:
        if active_step == GENERATE_MNEMONIC_STEP:
            set_mnemonic(AVAILABLE_MNEMONICS['24'])
            unlock()

        print("Button C pressed")

# set the buttons events
m5stack.ButtonA(callback=button_handler_a)
m5stack.ButtonB(callback=button_handler_b)
m5stack.ButtonC(callback=button_handler_c)


def generate_mnemonic():
    clean_screen()
    print_line_1("Choose mnemonic words")
    print_button_a('12 words')
    print_button_b('18 words')
    print_button_c('24 words')

def show_mnemonic():
    clean_screen()
    print_line_1("Write down your mnemonic:")

    # to fit into the screen we need to divide it into two array
    arr_mnemonic = mnemonic.split(' ')
    first = arr_mnemonic[:len(arr_mnemonic)//2]
    second = arr_mnemonic[len(arr_mnemonic)//2:]
    print_line_2(" ".join(first))
    print_line_3(" ".join(second))
    print_button_a('Continue')


def guess_word():
    clean_screen()
    print_line_1("WORK IN PROGRESS")

def display_menu():
    pass

def save():
    pass

def clean_screen():
    clear = '                                               '
    print_line_1(clear)
    print_line_2(clear)
    print_line_3(clear)
    print_button_a(clear)
    print_button_b(clear)
    print_button_c(clear)


def main():
    global active_step

    available_steps = {
        GENERATE_MNEMONIC_STEP: generate_mnemonic,
        SHOW_MNEMONIC_STEP: show_mnemonic,
        GUESS_WORD_STEP: guess_word,
        DISPLAY_MENU_STEP: display_menu,
        END_STEP: save
    }

    global lock

    while True:
        lock = True
        available_steps[active_step]()

        while lock:
            time.sleep_ms(500)

        # after unlock go to next step
        active_step += 1
        print(active_step)



if __name__ == '__main__':
    print_title("Welcome to the buidl wallet!")
    main()
