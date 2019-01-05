import sys
import serial

def send_msg(ser, data):
    msg = int.to_bytes(len(data), 4, 'little') + data
    return ser.write(msg)

def read_msg(stream):
    # msg_len = int.from_bytes(stream.read(4), 'little')
    # print(msg_len)
    return stream.read(10)

def main(port, msg):
    with serial.Serial(port) as ser:
        ser.baudrate = 115200
        ser.bytesize=serial.EIGHTBITS
        ser.parity=serial.PARITY_NONE
        ser.stopbits=serial.STOPBITS_ONE
        # ser.xonxoff=1
        # ser.rtscts=0
        print(ser)
        print(ser.write(b"abc\n"))
        print("sent")
        res = ser.read(3)
        print("response: ", res)

if __name__ == "__main__":
    _, port, msg = sys.argv
    main(port, msg)
