import string

def is_valid_key(key: str) -> bool:
    """Validates that the key contains 26 unique alphabetic characters."""
    return len(key) == 26 and set(key.upper()) == set(string.ascii_uppercase)

def encrypt(plaintext: str, key: str) -> str:
    """Encrypts plaintext using the 26-letter substitution key."""
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    cipher_alphabet = key.lower() + key.upper()
    
    # Create a character-to-character translation table
    translation_table = str.maketrans(alphabet, cipher_alphabet)
    return plaintext.translate(translation_table)

def decrypt(ciphertext: str, key: str) -> str:
    """Decrypts ciphertext back to plaintext using the substitution key."""
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    cipher_alphabet = key.lower() + key.upper()
    
    # Reverse the translation table for decryption
    reverse_table = str.maketrans(cipher_alphabet, alphabet)
    return ciphertext.translate(reverse_table)

def main():
    # Example key: A->Q, B->W, C->E, etc.
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"

    if not is_valid_key(key):
        print("Error: The key must contain 26 unique alphabetic characters.")
        return

    print(f"Substitution Key: {key}")
    plaintext = input("Enter a message to encrypt: ")

    ciphertext = encrypt(plaintext, key)
    print(f"\nEncrypted Message: {ciphertext}")

    decrypted = decrypt(ciphertext, key)
    print(f"Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
