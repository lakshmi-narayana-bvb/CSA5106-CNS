def decrypt_gold_bug():
    # The ciphertext from "The Gold-Bug"
    ciphertext = (
        "53±t+305))6*;4826)4.)4±);806*;48+860))85;;]8*::*8+83"
        "(88)5*+:46(;88*96*?:8)*t(;485):5*+2:**(:4956*2(5*_4)88*"
        ";4069285);)6+8)4*t;1(+9;48081;8:8†1;48†85;4)485+528806*81"
        "(9;48;(88;4(?34;48)4t;161;:188;?;"
    )

    # Substitution key mapping cipher symbols to English letters
    # Includes OCR/copy-paste variations present in your prompt (like ±, t, and _)
    key = {
        '8': 'E', ';': 'T', '4': 'H', ')': 'O', '6': 'S',
        '*': 'N', '5': 'A', '(': 'I', 't': 'R', '+': 'U',
        '0': 'O', '9': 'M', '2': 'D', ':': 'L', '3': 'Y',
        '1': 'C', '?': 'G', ']': 'P', '.': 'B', '-': 'V',
        '±': 'G', '†': 'D', '_': 'F'
    }

    # Build the decrypted string using a generator expression
    # If a character isn't in the key, keep it as-is
    decrypted_text = "".join(key.get(char, char) for char in ciphertext)

    print("Decoded Plaintext:\n")
    print(decrypted_text)

if __name__ == "__main__":
    decrypt_gold_bug()
