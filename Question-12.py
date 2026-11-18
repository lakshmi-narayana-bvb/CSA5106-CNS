import numpy as np

def mod_inverse(a, m=26):
    """Find modular multiplicative inverse of a under modulo m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Modular inverse does not exist for {a} mod {m}")

def get_inverse_key_matrix(key_matrix, mod=26):
    """Compute the inverse of a 2x2 matrix under modulo 26."""
    det = int(round(np.linalg.det(key_matrix))) % mod
    det_inv = mod_inverse(det, mod)
    
    # Adjugate matrix for 2x2: [[d, -b], [-c, a]]
    adj_matrix = np.array([
        [key_matrix[1][1], -key_matrix[0][1]],
        [-key_matrix[1][0], key_matrix[0][0]]
    ])
    
    inv_key = (det_inv * adj_matrix) % mod
    return inv_key.astype(int)

def prepare_text(text):
    """Remove non-alphabetic characters, convert to lowercase, and pad with 'x'."""
    clean_text = ''.join(char.lower() for char in text if char.isalpha())
    if len(clean_text) % 2 != 0:
        clean_text += 'x'
    return clean_text

def hill_cipher(text, key_matrix):
    """Encrypt or decrypt text using a 2x2 key matrix."""
    result = []
    for i in range(0, len(text), 2):
        # Convert letter pair to column vector
        pair = np.array([[ord(text[i]) - ord('a')], [ord(text[i+1]) - ord('a')]])
        # Matrix multiplication mod 26
        transformed = np.dot(key_matrix, pair) % 26
        # Convert back to letters
        result.append(chr(int(transformed[0][0]) + ord('a')))
        result.append(chr(int(transformed[1][0]) + ord('a')))
    return ''.join(result)

# --- Execution ---
if __name__ == "__main__":
    plaintext = "meet me at the usual place at ten rather than eight oclock"
    key = np.array([[9, 4], 
                    [5, 7]])

    # 1. Prepare and Encrypt
    prepared_text = prepare_text(plaintext)
    ciphertext = hill_cipher(prepared_text, key)

    # 2. Compute Inverse Key and Decrypt
    inv_key = get_inverse_key_matrix(key)
    decrypted_text = hill_cipher(ciphertext, inv_key)

    print(f"Prepared Plaintext : {prepared_text}")
    print(f"Ciphertext         : {ciphertext}")
    print(f"Inverse Key Matrix :\n{inv_key}")
    print(f"Decrypted Text     : {decrypted_text}")
