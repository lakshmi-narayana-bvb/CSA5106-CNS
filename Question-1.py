def caesar_cipher(text: str, k: int) -> str:
    result = []

    for ch in text:
        if ch.isupper():
            # Shift uppercase letters
            shifted = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted)
        elif ch.islower():
            # Shift lowercase letters
            shifted = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)
        else:
            # Keep spaces, numbers, and symbols unchanged
            result.append(ch)

    return "".join(result)


def main():
    message = input("Enter a message to encrypt: ")
    
    try:
        k = int(input("Enter shift key k (1-25): "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    # Validate the shift key range
    if k < 1 or k > 25:
        print("Invalid key! Please enter a value between 1 and 25.")
        return

    encrypted_message = caesar_cipher(message, k)
    print(f"Encrypted message: {encrypted_message}")


if __name__ == "__main__":
    main()
