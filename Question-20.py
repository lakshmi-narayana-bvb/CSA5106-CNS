BLOCK_SIZE = 8

def xor_block_cipher(block: bytes, key: bytes) -> bytes:
    """Simple XOR-based block cipher for demonstration."""
    return bytes([b ^ k for b, k in zip(block, key)])

def ecb_encrypt(plaintext: bytes, key: bytes) -> bytearray:
    ciphertext = bytearray()
    for i in range(0, len(plaintext), BLOCK_SIZE):
        block = plaintext[i:i + BLOCK_SIZE]
        ciphertext.extend(xor_block_cipher(block, key))
    return ciphertext

def ecb_decrypt(ciphertext: bytes, key: bytes) -> bytearray:
    decrypted = bytearray()
    for i in range(0, len(ciphertext), BLOCK_SIZE):
        block = ciphertext[i:i + BLOCK_SIZE]
        decrypted.extend(xor_block_cipher(block, key))
    return decrypted

def main():
    # 24 bytes = 3 blocks of 8 bytes each
    plaintext = b"BLOCK_1_BLOCK_2_BLOCK_3_"
    key = b"MYSECRET"

    # 1. Encrypt in ECB mode
    ciphertext = ecb_encrypt(plaintext, key)

    # 2. Introduce a transmission error in Ciphertext Block 1 (byte index 0)
    ciphertext[0] ^= 0xFF

    # 3. Decrypt in ECB mode
    decrypted = ecb_decrypt(ciphertext, key)

    print("Original Plaintext :", plaintext.decode('utf-8'))
    print("Decrypted Output   :", decrypted.decode('utf-8', errors='replace'))
    print("Notice that only Block 1 is corrupted; Block 2 and Block 3 remain intact.")

if __name__ == "__main__":
    main()
