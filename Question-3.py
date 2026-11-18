def generate_key_table(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix_list = []

    # Add unique letters from the keyword
    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            matrix_list.append(char)

    # Fill the rest of the matrix with remaining alphabet letters (excluding J)
    for code in range(ord('A'), ord('Z') + 1):
        char = chr(code)
        if char != 'J' and char not in seen:
            seen.add(char)
            matrix_list.append(char)

    # Convert the flat list of 25 characters into a 5x5 grid
    key_table = [matrix_list[i:i + 5] for i in range(0, 25, 5)]
    return key_table


def find_position(key_table, char):
    if char == 'J':
        char = 'I'
    for row in range(5):
        for col in range(5):
            if key_table[row][col] == char:
                return row, col
    return None


def prepare_text(plaintext):
    # Keep only alphabetic characters, convert to uppercase, and replace J with I
    clean = [c.upper().replace('J', 'I') for c in plaintext if c.isalpha()]
    prepared = []
    i = 0

    while i < len(clean):
        first = clean[i]
        if i + 1 < len(clean):
            second = clean[i + 1]
            if first == second:
                # Insert 'X' between identical consecutive letters
                prepared.extend([first, 'X'])
                i += 1
            else:
                prepared.extend([first, second])
                i += 2
        else:
            # Pad with 'X' if a single letter remains at the end
            prepared.extend([first, 'X'])
            i += 1

    return "".join(prepared)


def encrypt(prepared_text, key_table):
    ciphertext = []

    for i in range(0, len(prepared_text), 2):
        r1, c1 = find_position(key_table, prepared_text[i])
        r2, c2 = find_position(key_table, prepared_text[i + 1])

        if r1 == r2:
            # Rule 1: Same row -> shift right
            ciphertext.append(key_table[r1][(c1 + 1) % 5])
            ciphertext.append(key_table[r2][(c2 + 1) % 5])
        elif c1 == c2:
            # Rule 2: Same column -> shift down
            ciphertext.append(key_table[(r1 + 1) % 5][c1])
            ciphertext.append(key_table[(r2 + 1) % 5][c2])
        else:
            # Rule 3: Rectangle -> swap columns
            ciphertext.append(key_table[r1][c2])
            ciphertext.append(key_table[r2][c1])

    return "".join(ciphertext)


def main():
    key = input("Enter the keyword: ")
    plaintext = input("Enter the plaintext: ")

    key_table = generate_key_table(key)

    print("\n5x5 Playfair Key Matrix:")
    for row in key_table:
        print(" ".join(row))

    prepared = prepare_text(plaintext)
    print(f"\nPrepared Plaintext (Digraphs): {prepared}")

    ciphertext = encrypt(prepared, key_table)
    print(f"Ciphertext: {ciphertext}")


if __name__ == "__main__":
    main()
