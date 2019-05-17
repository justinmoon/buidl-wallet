import utime
import machine
import tcc

import m5stack

tft = m5stack.Display()


def double_sha256(message: bytes) -> bytes:
    return tcc.sha256(tcc.sha256(message).digest()).digest()


def send_msg(data):
    try:
        msg = int.to_bytes(len(data), 4, 'little') + data
        return machine.stdout_put(msg)
    except Exception as e:
        tft.text(tft.CENTER, 75, "str: %s" % str(e))


def read_msg():
    raw = machine.stdin_get(4, 100)
    tft.text(tft.CENTER, 25, str(raw))
    if raw:
        try:
            msg_len = int.from_bytes(raw.encode(), 'little')
        except Exception as e:
            return str(e)
        return machine.stdin_get(msg_len, 100)


def demo():
    tft.text(tft.CENTER, 5, "loaded")
    while True:
        msg = machine.stdin_get(3, 1000).encode()
        if msg:
            # hashed = double_sha256(msg)
            tft.clearwin()
            tft.text(tft.CENTER, 35, msg)
            # tft.text(tft.CENTER, 5, hashed)
            machine.stdout_put(b'xyz')
            utime.sleep(3)


def demo_input():
    uart = machine.UART(2, tx=17, rx=16)
    height = 0
    while True:
        msg = uart.readline().strip()
        tft.text(tft.CENTER, height, msg)
        height += 10
        print('rcv')


# if __name__ == '__main__':
    # demo_input()
