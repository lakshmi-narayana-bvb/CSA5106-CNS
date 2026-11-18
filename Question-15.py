import string

# Standard English letter frequencies (A-Z in percentages)
ENGLISH_FREQ = [
    8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094,
    6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929,
    0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150,
    1.974, 0.074
]

def decrypt(ciphertext: str, shift: int) -> str:
    """Decrypts text using an additive (Caesar) cipher with a given shift."""
    result = []
    for char in ciphertext:
        if char.isupper():
            result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        else:
            result.append(char)
    return "".join(result)

def score_text(text: str) -> float:
    """Scores candidate plaintext against standard English letter frequencies."""
    letters = [c.lower() for c in text if c.isalpha()]
    total_letters = len(letters)
    
    if total_letters == 0:
        return 0.0

    score = 0.0
    for i, letter in enumerate(string.ascii_lowercase):
        observed_pct = (letters.count(letter) / total_letters) * 100.0
        score += observed_pct * ENGLISH_FREQ[i]
    return score

def main():
    ciphertext = input("Enter the ciphertext: ").strip()
    if not ciphertext:
        print("No ciphertext provided.")
        return

    user_limit = input("How many top possible plaintexts would you like to see? (default 10): ").strip()
    try:
        top_n = int(user_limit) if user_limit else 10
        top_n = max(1, min(26, top_n))
    except ValueError:
        top_n = 10

    # Generate all 26 candidates and compute their likelihood scores
    candidates = []
    for shift in range(26):
        plaintext = decrypt(ciphertext, shift)
        likelihood = score_text(plaintext)
        candidates.append((likelihood, shift, plaintext))

    # Sort candidates from highest score to lowest
    candidates.sort(key=lambda x: x[0], reverse=True)

    print(f"\nTop {top_n} possible plaintexts in order of likelihood:")
    for rank, (score, shift, plaintext) in enumerate(candidates[:top_n], start=1):
        print(f"{rank}. [Shift {shift:2d}] -> {plaintext}")

if __name__ == "__main__":
    main()
