import math

def solve_affine_keys(c1_char, c2_char, p1_char='E', p2_char='T'):
    # Convert characters to 0-25 numeric values
    p1 = ord(p1_char.upper()) - ord('A')  # 4 ('E')
    p2 = ord(p2_char.upper()) - ord('A')  # 19 ('T')
    c1 = ord(c1_char.upper()) - ord('A')  # 1 ('B')
    c2 = ord(c2_char.upper()) - ord('A')  # 20 ('U')

    diff_p = (p2 - p1) % 26  # 15
    diff_c = (c2 - c1) % 26  # 19

    # Solve for 'a' where (diff_p * a) % 26 == diff_c and gcd(a, 26) == 1
    a = None
    for candidate_a in range(1, 26):
        if math.gcd(candidate_a, 26) == 1:
            if (diff_p * candidate_a) % 26 == diff_c:
                a = candidate_a
                break

    if a is None:
        raise ValueError("Could not find a valid key 'a'.")

    # Solve for 'b' where (a * p1 + b) % 26 == c1
    b = (c1 - a * p1) % 26
    return a, b

def decrypt_affine(ciphertext, a, b):
    # Python 3.8+ built-in modular inverse: pow(a, -1, 26)
    a_inv = pow(a, -1, 26)
    plaintext = []

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            c = ord(char) - base
            
            # Decryption formula: P = a^-1 * (C - b) mod 26
            p = (a_inv * (c - b)) % 26
            plaintext.append(chr(p + base))
        else:
            # Keep spaces and punctuation unchanged
            plaintext.append(char)

    return "".join(plaintext)

if __name__ == "__main__":
    # Find keys using most frequent ('B') and second most frequent ('U')
    a, b = solve_affine_keys('B', 'U')
    a_inv = pow(a, -1, 26)
    print(f"Solved Keys -> a = {a}, b = {b} (Modular Inverse a^-1 = {a_inv})")

    # Decrypt user-provided ciphertext
    ciphertext = input("Enter the ciphertext to decrypt: ")
    decrypted_text = decrypt_affine(ciphertext, a, b)
    print(f"Decrypted Plaintext: {decrypted_text}")
