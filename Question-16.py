from collections import Counter

# Standard English letter frequency order from most to least frequent
ENGLISH_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def decrypt_by_shift(ciphertext: str, shift: int) -> str:
    """Decrypts text using a shift offset while preserving case and punctuation."""
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            val = (ord(char) - base - shift) % 26
            plaintext.append(chr(base + val))
        else:
            plaintext.append(char)
    return "".join(plaintext)

def frequency_attack():
    ciphertext = input("Enter the ciphertext: ").strip()
    if not ciphertext:
        print("Error: Ciphertext cannot be empty.")
        return

    try:
        top_n = int(input("How many top possible plaintexts would you like to see? (e.g., 10): "))
        if not (1 <= top_n <= 26):
            top_n = 10
    except ValueError:
        top_n = 10

    # Extract only alphabetic characters and convert to uppercase
    letters_only = [c.upper() for c in ciphertext if c.isalpha()]
    if not letters_only:
        print("No alphabetic characters found in the ciphertext.")
        return

    # Find the most frequent letter in the ciphertext
    most_common_cipher_char, _ = Counter(letters_only).most_common(1)[0]

    print(f"\nTop {top_n} possible plaintexts:")
    print("-" * 40)

    for i in range(top_n):
        target_english_char = ENGLISH_FREQ[i]
        shift = (ord(most_common_cipher_char) - ord(target_english_char)) % 26
        candidate = decrypt_by_shift(ciphertext, shift)
        
        print(f"Candidate {i + 1} (Shift {shift}, assuming '{most_common_cipher_char}' -> '{target_english_char}'): {candidate}")

if __name__ == "__main__":
    frequency_attack()
