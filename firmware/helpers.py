import tcc
import urandom

SIGHASH_ALL = 1
SIGHASH_NONE = 2
SIGHASH_SINGLE = 3
BASE58_ALPHABET = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def double_sha256(message: bytes) -> bytes:
    return tcc.sha256(tcc.sha256(message).digest()).digest()

def entropy(n: int):
    # TODO: hardware RNG
    return bytes([urandom.getrandbits(8) for _ in range(n)])

def decode_base58(s):
    num = 0
    for c in s.encode('ascii'):
        num *= 58
        num += BASE58_ALPHABET.index(c)
    combined = num.to_bytes(25, byteorder='big')
    checksum = combined[-4:]
    if double_sha256(combined[:-4])[:4] != checksum:
        raise RuntimeError('bad address: {} {}'.format(checksum, double_sha256(combined)[:4]))
    return combined[1:-4]

# def encode_varint(i):
    # '''encodes an integer as a varint'''
    # if i < 0xfd:
        # return bytes([i])
    # elif i < 0x10000:
        # return b'\xfd' + int_to_little_endian(i, 2)
    # elif i < 0x100000000:
        # return b'\xfe' + int_to_little_endian(i, 4)
    # elif i < 0x10000000000000000:
        # return b'\xff' + int_to_little_endian(i, 8)
    # else:
        # raise RuntimeError('integer too large: {}'.format(i))

def little_endian_to_int(b):
    '''little_endian_to_int takes byte sequence as a little-endian number.
    Returns an integer'''
    # use the from_bytes method of int
    return int.from_bytes(b, 'little')


def int_to_little_endian(n, length):
    '''endian_to_little_endian takes an integer and returns the little-endian
    byte sequence of length'''
    # use the to_bytes method of n
    return n.to_bytes(length, 'little')

def p2pkh_script(h160):
    '''Takes a hash160 and returns the scriptPubKey'''
    return b'\x76\xa9\x14' + h160 + b'\x88\xac'

def read_varint(s):
    '''read_varint reads a variable integer from a stream'''
    i = s.read(1)[0]
    if i == 0xfd:
        # 0xfd means the next two bytes are the number
        return little_endian_to_int(s.read(2))
    elif i == 0xfe:
        # 0xfe means the next four bytes are the number
        return little_endian_to_int(s.read(4))
    elif i == 0xff:
        # 0xff means the next eight bytes are the number
        return little_endian_to_int(s.read(8))
    else:
        # anything else is just the integer
        return i

# Mine

def reverse_bytes(b):
    reversed = b""
    for x in b:
        reversed = reversed + chr(x)
    return reversed

