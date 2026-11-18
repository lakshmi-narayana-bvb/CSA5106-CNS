import math

def mod_inverse(a, m=26):
    """Find the modular multiplicative inverse of 'a' under modulo 'm'."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt_affine(text, a, b):
    """Encrypt plaintext using C = (a*p + b) mod 26."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            p = ord(char) - base
            c = (a * p + b) % 26
            result.append(chr(c + base))
        else:
            result.append(char)
    return "".join(result)

def decrypt_affine(cipher, a, b):
    """Decrypt ciphertext using P = a^-1 * (c - b) mod 26."""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Invalid key 'a': no modular inverse exists.")
    
    result = []
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            c = ord(char) - base
            p = (a_inv * (c - b)) % 26
            result.append(chr(p + base))
        else:
            result.append(char)
    return "".join(result)

# Main execution
if __name__ == "__main__":
    message = input("Enter the message: ")
    a = int(input("Enter key 'a': "))
    
    # Validate that 'a' is coprime with 26
    if math.gcd(a, 26) != 1:
        print("Error: Invalid value for 'a'. It must be coprime with 26 (not even and not a multiple of 13).")
    else:
        b = int(input("Enter key 'b': "))
        
        encrypted = encrypt_affine(message, a, b)
        print(f"Encrypted Ciphertext: {encrypted}")
        
        decrypted = decrypt_affine(encrypted, a, b)
        print(f"Decrypted Plaintext:  {decrypted}")
