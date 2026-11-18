# 5x5 Playfair Matrix (I and J share the same cell; 'I' represents both)
matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

def find_position(ch):
    if ch == 'J':
        ch = 'I'
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
    return None

def prepare_message(text):
    # Keep only uppercase letters and convert J to I
    clean = [c.upper() if c.upper() != 'J' else 'I' for c in text if c.isalpha()]
    
    # Split into digraphs, inserting 'X' between identical pairs
    prepared = []
    i = 0
    while i < len(clean):
        prepared.append(clean[i])
        if i + 1 < len(clean):
            if clean[i] == clean[i + 1]:
                prepared.append('X')
                i += 1
            else:
                prepared.append(clean[i + 1])
                i += 2
        else:
            i += 1

    # Pad with 'X' if total length is odd
    if len(prepared) % 2 != 0:
        prepared.append('X')
        
    return "".join(prepared)

def encrypt_playfair(prepared):
    cipher = []
    for i in range(0, len(prepared), 2):
        r1, c1 = find_position(prepared[i])
        r2, c2 = find_position(prepared[i + 1])

        if r1 == r2:
            # Same row: shift right
            cipher.append(matrix[r1][(c1 + 1) % 5])
            cipher.append(matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:
            # Same column: shift down
            cipher.append(matrix[(r1 + 1) % 5][c1])
            cipher.append(matrix[(r2 + 1) % 5][c2])
        else:
            # Rectangle: swap columns
            cipher.append(matrix[r1][c2])
            cipher.append(matrix[r2][c1])

    return "".join(cipher)

if __name__ == "__main__":
    message = "Must see you over Cadogan West. Coming at once."
    prepared = prepare_message(message)
    cipher = encrypt_playfair(prepared)

    digraphs = " ".join(prepared[i:i+2] for i in range(0, len(prepared), 2))
    print("Original Message :", message)
    print("Prepared Digraphs:", digraphs)
    print("Encrypted Output :", cipher)
