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

def demo():
    while True:
        msg = machine.stdin_get(3, 1000)
        if msg:
            tft.clearwin()
            tft.text(tft.CENTER, 35, msg)
            machine.stdout_put(b"xyz")
            utime.sleep(3)

if __name__ == '__main__':
    demo()
