import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def encrypt_3des_cbc(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    # Apply PKCS7 padding to match 3DES block size (64 bits / 8 bytes)
    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Initialize 3DES cipher in CBC mode
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext


def decrypt_3des_cbc(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    # Initialize 3DES cipher in CBC mode for decryption
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    # Decrypt and remove PKCS7 padding
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext


if __name__ == "__main__":
    # 24-byte (192-bit) key for 3-key 3DES (K1 || K2 || K3)
    key = os.urandom(24)

    # 8-byte (64-bit) random Initialization Vector (IV)
    iv = os.urandom(8)

    message = b"Confidential message encrypted using 3DES in CBC mode."

    # Encrypt and decrypt
    encrypted = encrypt_3des_cbc(message, key, iv)
    decrypted = decrypt_3des_cbc(encrypted, key, iv)

    print(f"Key (Hex):        {key.hex()}")
    print(f"IV (Hex):         {iv.hex()}")
    print(f"Ciphertext (Hex): {encrypted.hex()}")
    print(f"Decrypted Text:   {decrypted.decode('utf-8')}")
