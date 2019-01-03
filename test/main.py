import m5stack
import tcc


def sign_and_verify():
    node = tcc.bip32.from_seed(b"foo", "secp256k1")
    private_key = node.private_key()
    public_key = node.public_key()
    message = "hi"
    message_digest = tcc.sha256(message).digest()
    sig = tcc.secp256k1.sign(private_key, message_digest)
    verifies = tcc.secp256k1.verify(public_key, sig, message_digest)
    return verifies


def main():
    tft = m5stack.Display()
    verifies = sign_and_verify
    message = "verifies? %s" % verifies
    tft.text(tft.CENTER, 45, "verifies")


if __name__ == "__main__":
    main()
 
