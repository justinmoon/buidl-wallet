import urandom

import tcc
import m5stack




SEED_FILE = "seed.txt"


def double_sha256(message: bytes) -> bytes:
    return tcc.sha256(tcc.sha256(message).digest()).digest()

def entropy(n: int):
    # TODO: hardware RNG
    return bytes([urandom.getrandbits(8) for _ in range(n)])

def derive_node(seed, path: list, curve_name: str = "secp256k1") -> tcc.bip32.HDNode:
    print(seed)
    node = tcc.bip32.from_seed(seed, curve_name)
    # TODO: node.derive_path(path)
    return node

def sign_message(node: tcc.bip32.HDNode, message: bytes) -> bytes:
    private_key = node.private_key()
    message_digest = double_sha256(message)
    sig = tcc.secp256k1.sign(private_key, message_digest)
    return sig

def verify(node: tcc.bip32.HDNode, signature: bytes, message: bytes) -> bool:
    public_key = node.public_key()
    message_digest = double_sha256(message)
    return tcc.secp256k1.verify(public_key, signature, message_digest)

def save_seed_to_disk(seed):
    open(SEED_FILE, "wb").write(seed)

def init_device():
    data = entropy(32)
    print("bip39 entropy=", data)
    mnemonic = tcc.bip39.from_data(data)
    print("mnemonic=", mnemonic)
    passphrase = ""
    seed = tcc.bip39.seed(mnemonic, passphrase)
    print("seed=", seed)
    save_seed_to_disk(seed)

def load_seed_from_disk():
    return open(SEED_FILE, 'rb').read()

def sign_and_verify(seed):
    path = [0, 0, 0, 0]
    message = b"test"
    print("deriving node")
    node = derive_node(seed, path)
    print("signing...")
    sig = sign_message(node, message)
    verifies = verify(node, sig, message)
    print("verifies?", verifies)
    return verifies

def init():
    init_device()
    print("saved seed to disk")

def boot():
    seed = load_seed_from_disk()
    print("read seed from disk")
    return seed

def main():
    tft = m5stack.Display()

    init()
    seed = boot()
    try:
        verifies = sign_and_verify(seed)
    except Exception as e:
        verifies = "error"
        import sys
        sys.print_exception(e)
    message = "verifies? %s" % verifies
    tft.text(tft.CENTER, 45, message)

if __name__ == '__main__':
    main()
