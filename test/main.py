import tcc


def test():
    node = tcc.bip32.from_seed(b"foo", "secp256k1")
    message = "hi"
    private_key = node.private_key()
    public_key = node.public_key()
    message_digest = tcc.sha256(message).digest()
    sig = tcc.secp256k1.sign(private_key, message_digest)
    verifies = tcc.secp256k1.verify(public_key, sig, message_digest)
    print(verifies)

