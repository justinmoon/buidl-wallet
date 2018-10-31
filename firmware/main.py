import uos
import tcc
import keys
import binascii
import m5stack

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

def print_seed(seed):
    hex_seed = binascii.hexlify(seed)
    print(hex_seed)
    counter = 0
    y = 45
    while counter < len(hex_seed):
        tft.text(tft.CENTER, y, hex_seed[counter:counter+20])
        counter += 20
        y += 20

def main():
    if keys.SEED_FILE not in uos.listdir('.'):
        print("Initializing wallet")
        init()
    print("Loading seed")
    seed = boot()
    print_seed(seed)
    sign_and_verify(seed)

if __name__ == '__main__':
    main()
