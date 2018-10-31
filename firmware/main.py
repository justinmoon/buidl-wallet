#
# # This file is part of MicroPython M5Stack package
# Copyright (c) 2017-2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-m5stack
#

#pylint: disable=import-error
# from machine import Pin, SPI
# from input import DigitalInput
# import display
# import m5stack
#pylint: enable=import-error

# tft = m5stack.Display()

# tft.text(tft.CENTER, 45,        "`7MMM.     ,MMF'       \n")
# tft.text(tft.CENTER, tft.LASTY, "  MMMb    dPMM         \n")
# tft.text(tft.CENTER, tft.LASTY, "  M YM   ,M MM  M******\n")
# tft.text(tft.CENTER, tft.LASTY, "  M  Mb  M' MM .M      \n")
# tft.text(tft.CENTER, tft.LASTY, "  M  YM.P'  MM |bMMAg. \n")
# tft.text(tft.CENTER, tft.LASTY, "  M  `YM'   MM      `Mb\n")
# tft.text(tft.CENTER, tft.LASTY, ".JML. `'  .JMML.     jM\n")
# tft.text(tft.CENTER, tft.LASTY, "               (O)  ,M9\n")
# tft.text(tft.CENTER, tft.LASTY, "                6mmm9  \n")
# tft.text(tft.CENTER, tft.LASTY, "                       \n")
# tft.text(tft.CENTER, tft.LASTY, "https://appelsiini.net/")

# def button_handler_a(pin, pressed):
    # if pressed is True:
        # tft.text(
            # tft.CENTER, tft.LASTY, "> Button A pressed.     "
        # )
        # m5stack.tone(1800, duration=10, volume=1)
    # else:
        # tft.text(
            # tft.CENTER, tft.LASTY, "> Button A released.    "
        # )
        # m5stack.tone(1300, duration=10, volume=1)

# def button_handler_b(pin, pressed):
    # if pressed is True:
        # tft.text(
            # tft.CENTER, tft.LASTY, "> Button B pressed.     "
        # )
        # m5stack.tone(2000, duration=10, volume=1)
    # else:
        # tft.text(
            # tft.CENTER, tft.LASTY, "> Button B released.    "
        # )
        # m5stack.tone(1500, duration=10, volume=1)

# def button_handler_c(pin, pressed):
    # if pressed is True:
        # tft.text(
            # tft.CENTER, tft.LASTY, "> Button C pressed.     "
        # )
        # m5stack.tone(2200, duration=10, volume=1)
    # else:
        # tft.text(
            # tft.CENTER, tft.LASTY, "> Button C released.    "
        # )
        # m5stack.tone(1800, duration=10, volume=1)

# a = m5stack.ButtonA(callback=button_handler_a)
# b = m5stack.ButtonB(callback=button_handler_b)
# c = m5stack.ButtonC(callback=button_handler_c)


import uos
import tcc
import keys
# import display
import m5stack
#pylint: enable=import-error

tft = m5stack.Display()


def sign_and_verify(seed):
    path = "m/2147431408'/0'/0'".split("/")
    message = b"test"
    print("deriving node")
    node = keys.derive_node(seed, path)
    print("signing...")
    # sig = keys.sign_message(node, message)
    # verifies = keys.verify(node, sig, message)
    # print("verifies?")
    # print(verifies)
    # tft.text(tft.CENTER, 45, "verifies? {verifies}")

def init():
    keys.init_device()
    print("saved seed to disk")

def boot():
    seed = keys.load_seed_from_disk()
    print("read seed from disk")
    return seed

def main():
    tft.text(tft.CENTER, 45, "Hello, world")
    # if keys.SEED_FILE not in uos.listdir('.'):
        # init()
    # seed = boot()
    # sign_and_verify(seed)




if __name__ == '__main__':
    main()
