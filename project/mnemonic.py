import urandom
import tcc
import m5stack

PATH = [44 | 0x80000000, 17 | 0x00000000, 0 | 0x00000000, 0, 0]
STEPS = ['mnemonic', 'seed', 'node', 'address']

current_step = 0

m5stack.ButtonA(
    callback=lambda pin, pressed: current_step += 1))
)


def entropy(n: int):
    return bytes([urandom.getrandbits(8) for _ in range(n)])

# def node_derive(root, path):
#     node = root.clone()
#     node.derive_path(path)
#     return node

def generate_mnemonic():
    data = entropy(32)
    print("bip39 entropy=", data)
    mnemonic = tcc.bip39.from_data(data)
    print("mnemonic=", mnemonic)
    return mnemonic

def generate_seed():
    tcc.bip39.seed(mnemonic, "")
    print("seed=", seed)
    return seed


def start():
    m5stack.lcd.clear()
    m5stack.lcd.setCursor(0, 0)

    # generate 12 words seed
    mnemonic = generate_mnemonic()
    print(mnemonic)

    # wait for click

    # Generate the seed from the mnemonic
    seed = generate_seed(mnemonic)
    print(seed)

    # wait for click

    # Generate the root
    root = tcc.bip32.from_seed(seed, "secp256k1")
    print(root)

    # wait for click

    # Generate node
    node = tcc.apps.wallet.sign_tx.addresses.node_derive(root, PATH)
    print(node)

    # wait for click

    # Generate the p2phk address
    # address ex: mhcZr15xutLwvWzrxVEhLXkb9bLcTaZN6e
    # bitcoin is address_type 0
    # https://github.com/trezor/trezor-core/blob/master/src/apps/common/coininfo.py
    address = node.address(address_type = 0)
    print(address)


if __name__ == '__main__':
    tft = m5stack.Display()
    start()
