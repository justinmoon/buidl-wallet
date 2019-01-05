import utime
import machine

import m5stack

tft = m5stack.Display()

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

def log(msg):
    with open("log.txt") as f:
        f.write(msg)

def loboris():
    # tft.text(tft.CENTER, 45, 'fuck me')
    index = 0
    while True:
        # machine.stdin_disable(b"\x11")
        msg = machine.stdin_get(10, 1000)
        tft.clearwin()
        tft.text(tft.CENTER, 35, str(index))
        if msg:
        # log(str(msg))
        # tft.text(tft.CENTER, 45, 'Read: "%s"' % msg)
            tft.text(tft.CENTER, 45, "type: %s" % type(msg))
            tft.text(tft.CENTER, 55, "len: %s" % len(msg))
            tft.text(tft.CENTER, 65, "set: %s" % set(msg))
            tft.text(tft.CENTER, 75, "str: %s" % msg)
            machine.stdout_put(b"xyz")
            # machine.stdin_put(b"niner")
            utime.sleep(3)
        else:
            tft.text(tft.CENTER, 45, "nada")
            utime.sleep(3)

        index += 1


def uart():
    # tft.text(tft.CENTER, 45, 'fuck me')
    # uart2 = machine.UART(1, rx=22, tx=41, timeout=100)
    uart2 = machine.UART(2)
    uart2.init(115200, bits=8, parity=None, stop=1)
    index = 0
    while True:
        tft.clearwin()
        tft.text(tft.CENTER, 35, str(index))
        
        msg = uart2.read(10)

        if msg:
            tft.text(tft.CENTER, 45, "type: %s" % type(msg))
            tft.text(tft.CENTER, 55, "len: %s" % len(msg))
            tft.text(tft.CENTER, 65, "set: %s" % set(msg))
            tft.text(tft.CENTER, 75, "str: %s" % msg)
            utime.sleep(3)
        else:
            tft.text(tft.CENTER, 45, str(msg))
            utime.sleep(3)

        index += 1


if __name__ == '__main__':
    loboris()
