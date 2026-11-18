def encrypt(plaintext: str, key: list[int]) -> str:
    """Encrypts plaintext using a numeric key stream."""
    ciphertext = []
    for p_char, k in zip(plaintext.lower(), key):
        p = ord(p_char) - ord('a')
        c = (p + k) % 26
        ciphertext.append(chr(c + ord('a')))
    return "".join(ciphertext)


def decrypt(ciphertext: str, key: list[int]) -> str:
    """Decrypts ciphertext using a numeric key stream."""
    plaintext = []
    for c_char, k in zip(ciphertext.lower(), key):
        c = ord(c_char) - ord('a')
        p = (c - k) % 26
        plaintext.append(chr(p + ord('a')))
    return "".join(plaintext)


def find_key(ciphertext: str, target_plaintext: str) -> list[int]:
    """Finds the key stream required to map ciphertext to a target plaintext."""
    derived_key = []
    for c_char, p_char in zip(ciphertext.lower(), target_plaintext.lower()):
        c = ord(c_char) - ord('a')
        p = ord(p_char) - ord('a')
        derived_key.append((c - p) % 26)
    return derived_key


if __name__ == "__main__":
    # Part (a)
    plaintext_a = "sendmoremoney"
    key_a = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

    ciphertext_a = encrypt(plaintext_a, key_a)
    print("Part (a)")
    print(f"Plaintext:  {plaintext_a}")
    print(f"Ciphertext: {ciphertext_a}\n")

    # Part (b)
    target_plaintext_b = "cashnotneeded"
    key_b = find_key(ciphertext_a, target_plaintext_b)
    decrypted_check = decrypt(ciphertext_a, key_b)

    print("Part (b)")
    print(f"Target Plaintext: {target_plaintext_b}")
    print(f"Derived Key:      {' '.join(map(str, key_b))}")
    print(f"Verification:     {decrypted_check}")
