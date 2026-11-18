# Initial Permutation (IP)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17,  9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Final Permutation (IP^-1)
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41,  9, 49, 17, 57, 25
]

# Expansion Table (E)
E = [
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
]

# Permutation Function (P)
P = [
    16,  7, 20, 21,
    29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
]

# Permuted Choice 1 (PC-1)
PC1 = [
    57, 49, 41, 33, 25, 17,  9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4
]

# Permuted Choice 2 (PC-2)
PC2 = [
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# Right-shift schedule for Decryption (generates K16 down to K1)
DECRYPT_SHIFTS = [0, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# S-Boxes
S_BOX = [
    [ # S1,
        [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
        [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
        [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
    ],
    [ # S2,
        [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
        [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
        [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]
    ],
    [ # S3,
 ,
 ,
        [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]
    ],
    [ # S4
        [ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
,
 ,
        [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]
    ],
    [ # S5
        [ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
,
        [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
        [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]
    ],
    [ # S6,
 ,
        [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
        [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]
    ],
    [ # S7
        [ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
,
        [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
        [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]
    ],
    [ # S8,
        [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
        [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
        [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]
    ]
]


def permute(value: int, table: list[int], input_bits: int) -> int:
    """Permutes bits of an integer according to a 1-based DES permutation table."""
    output = 0
    for pos in table:
        bit = (value >> (input_bits - pos)) & 1
        output = (output << 1) | bit
    return output


def right_rotate_28(val: int, shifts: int) -> int:
    """Performs a 28-bit circular right shift."""
    val &= 0x0FFFFFFF
    if shifts == 0:
        return val
    return ((val >> shifts) | (val << (28 - shifts))) & 0x0FFFFFFF


def generate_decryption_keys(key: int) -> list[int]:
    """Generates 16 round subkeys in reverse order (K16 down to K1)."""
    permuted_key = permute(key, PC1, 64)
    c = (permuted_key >> 28) & 0x0FFFFFFF
    d = permuted_key & 0x0FFFFFFF

    subkeys = []
    for shift in DECRYPT_SHIFTS:
        c = right_rotate_28(c, shift)
        d = right_rotate_28(d, shift)
        combined = (c << 28) | d
        subkeys.append(permute(combined, PC2, 56))

    return subkeys


def feistel(r: int, subkey: int) -> int:
    """DES Feistel (f) function."""
    expanded = permute(r, E, 32)
    xored = expanded ^ subkey

    sbox_output = 0
    for i in range(8):
        chunk = (xored >> (42 - i * 6)) & 0x3F
        row = ((chunk & 0x20) >> 4) | (chunk & 0x01)
        col = (chunk >> 1) & 0x0F
        sbox_output = (sbox_output << 4) | S_BOX[i][row][col]

    return permute(sbox_output, P, 32)


def des_decrypt(ciphertext: int, key: int) -> int:
    """Decrypts a 64-bit ciphertext block using a 64-bit key."""
    subkeys = generate_decryption_keys(key)

    # 1. Initial Permutation
    ip_block = permute(ciphertext, IP, 64)
    left = (ip_block >> 32) & 0xFFFFFFFF
    right = ip_block & 0xFFFFFFFF

    # 2. 16 Feistel rounds using K16 down to K1
    for subkey in subkeys:
        left, right = right, left ^ feistel(right, subkey)

    # 3. 32-bit Swap (R16 || L16) and Final Permutation
    pre_output = (right << 32) | left
    return permute(pre_output, FP, 64)


if __name__ == "__main__":
    # Standard DES Test Vector
    key = 0x133457799BBCDFF1
    ciphertext = 0x85E813540F0AB405  # Encrypts 0x0123456789ABCDEF

    plaintext = des_decrypt(ciphertext, key)

    print(f"Key:        0x{key:016X}")
    print(f"Ciphertext: 0x{ciphertext:016X}")
    print(f"Plaintext:  0x{plaintext:016X}")
