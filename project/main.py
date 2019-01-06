import m5stack

import mnemonic

tft = m5stack.Display()

def display_text():
    tft.text(tft.CENTER, 45,        "Choose your option:\n")
    tft.text(tft.CENTER, tft.LASTY, "A: Generate address,\n")
    tft.text(tft.CENTER, tft.LASTY, "B: Create a transaction,\n")

def init_mnemonic():
    mnemonic.start()

def init_transaction():
    pass

def set_buttons():
    a = m5stack.ButtonA(callback=init_mnemonic)
    b = m5stack.ButtonB(callback=init_transaction)

def start():
    display_text()
    set_buttons()


if __name__ == '__main__':
    start()
