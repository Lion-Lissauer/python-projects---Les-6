def caesar_cipher(text, shift, action="encode"):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if action == "encode":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif action == "decode":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def main():
    while True:
        action = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").strip().lower()
        if action not in ["encode", "decode"]:
            print("Input invalid, please try.")
            continue

        message = input("Enter message:\n")
        shift = int(input("Enter shift (0-25):\n"))

        result = caesar_cipher(message, shift, action)

        if action == "encode":
            print(f"the encoded text is: {result}")
        else:
            print(f"the decoded text is: {result}")

        again = input("Would you like to encrypt/decrypt again? (y/n)\n").strip().lower()
        if again != "y":
            print("Thanks for using this application")
            break

if __name__ == "__main__":
    main()