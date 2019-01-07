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
    12: 'together strong topple gown hospital people pig spend sport sweet choose solve'
    15: 'faint outer guitar switch ugly short dolphin cross print slogan permit mail object chief rally'
    18: 'when pool song man agree when hair ring undo weapon art number phone recycle journey drill word inherit'
    21: 'problem soccer valve sudden tribe crane legal notable fee fish find junior walk firm bench alpha pudding resemble actor security trade'
    24: 'tonight slim actress bargain wrestle debris warfare flight switch hero forget flip exercise put retire screen organ wisdom sick banner bench mask key identify'
}

active_step = 0
num_words_index = 0

m5stack.ButtonC(callback=lambda pin, pressed: increase_num_words()))

def next_step():
    if active_step < 4:
        active_step += 1
        print(AVAILABLE_STEPS[active_step])

def increase_num_words():
    if num_words_index < 5:
        num_words_index += 1
        print(AVAILABLE_NUM_WORDS[num_words_index])

def decrease_num_words():
    if num_words_index > 0:
        num_words_index -= 1
        print(AVAILABLE_NUM_WORDS[num_words_index])


def select_entropy():
    m5stack.lcd.clear()
    tft.text(tft.CENTER, 45, "Choose the number of words in the mnemonice")
    tft.text(tft.CENTER, 65, "Press A to increase")
    tft.text(tft.CENTER, 65, "Press B to decrease")
    tft.text(tft.CENTER, 65, "Press C to continue")

    m5stack.ButtonA(callback=lambda pin, pressed: increase_num_words()))
    m5stack.ButtonB(callback=lambda pin, pressed: increase_num_words()))

    while active_step == 0:
        pass

def main():
    tft.text(tft.CENTER, 45, "Welcome to the buidl wallet!")
    tft.text(tft.CENTER, 45, "Press A to continue.")

    # choose the entropy
    num_words = select_entropy()
    print(num_words)

    # generate the mnemonic (entropy)

    # guess the 5th word

    # display menu

    # user cli.py to sign a transtion


if __name__ == '__main__':
    main()
