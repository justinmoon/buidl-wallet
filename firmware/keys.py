import tcc
from helpers import entropy, double_sha256


SEED_FILE = "seed.txt"

def derive_node(seed, path: list, curve_name: str = "secp256k1") -> tcc.bip32.HDNode:
    print(seed)
    print(curve_name)
    node = tcc.bip32.from_seed(seed, curve_name)
    print(node)
    print(path)
    node.derive_path(path)
    return node

def sign_message(node: tcc.bip32.HDNode, message: bytes) -> bytes:
    private_key = node.private_key()
    print(private_key)
    message_digest = double_sha256(message)
    print(message_digest)
    sig = tcc.secp256k1.sign(private_key, message_digest)
    print(sig)
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
