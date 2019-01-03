import m5stack

tft = m5stack.Display()


def main():
    tft.text(tft.CENTER, 45, "hello, justin!")


if __name__ == '__main__':
    main()
