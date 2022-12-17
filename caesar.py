def encrypt(text, offset):
    result = ""

    # transverse the plain txt
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            char = chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
        elif (char.islower()):
            char = chr((ord(char) - ord('a') + offset) % 26 + ord('a'))

        result += char
    return result


def decrypt(text, offset):
    return encrypt(text, -offset)
