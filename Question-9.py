def generate_matrix(key):
    key = key.upper().replace(" ", "").replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix_chars = []
    
    # Add unique characters from the key
    for char in key:
        if char in alphabet and char not in matrix_chars:
            matrix_chars.append(char)
            
    # Add remaining characters from the alphabet
    for char in alphabet:
        if char not in matrix_chars:
            matrix_chars.append(char)
            
    # Reshape into a 5x5 grid
    return [matrix_chars[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    if char == 'J':
        char = 'I'
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return None

def decrypt_pair(matrix, a, b):
    r1, c1 = find_position(matrix, a)
    r2, c2 = find_position(matrix, b)
    
    if r1 == r2:
        # Same row: shift left
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:
        # Same column: shift up
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    else:
        # Rectangle rule: swap columns
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_playfair(ciphertext, key):
    matrix = generate_matrix(key)
    clean_cipher = "".join(c.upper() for c in ciphertext if c.isalpha())
    
    decrypted_pairs = []
    for i in range(0, len(clean_cipher), 2):
        pair = decrypt_pair(matrix, clean_cipher[i], clean_cipher[i+1])
        # Translate 'TT' into 'tt' as requested
        if pair == "TT":
            decrypted_pairs.append("tt")
        else:
            decrypted_pairs.append(pair)
            
    return "".join(decrypted_pairs)

if __name__ == "__main__":
    key = "ROYAL NEW ZEALAND NAVY"
    ciphertext = (
        "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO "
        "BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
    )
    
    result = decrypt_playfair(ciphertext, key)
    print("Decrypted Message:", result)
