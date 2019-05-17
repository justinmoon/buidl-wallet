import sys
import time

import serial


ser =  serial.Serial(
    sys.argv[1], baudrate=115200, bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE
)


counter = 0
while True:
    ser.write(counter.to_bytes(1, 'big'))
    print('wrote', counter)
    time.sleep(1)
    print(counter)
    counter += 1
