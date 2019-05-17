import utime
import machine
import m5stack


tft = m5stack.Display()
uart = machine.UART(2, tx=17, rx=16)


def main():
    while True:
        height = 0
        b = uart.read(1)
        tft.text(tft.CENTER, height, 'msg: ' + str(b))
        height += 10
        utime.sleep(1)

if __name__ == '__main__':
    main()
