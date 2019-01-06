import sys
import serial

def send_msg(ser, data):
    msg = int.to_bytes(len(data), 4, 'little') + data
    return ser.write(msg)

def read_msg(stream):
    # msg_len = int.from_bytes(stream.read(4), 'little')
    # print(msg_len)
    return stream.read(10)

def main(port):
    with serial.Serial(port, baudrate=115200, bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE) as ser:
        ser.write(b"abc")
        res = ser.read(3)
        print("response: ", res)

if __name__ == "__main__":
    port = sys.argv[1]
    main(port)
