def encrypt(message, offset):
    result = ""

    # transverse the plain txt
    for i in range(len(message)):
        char = message[i]

        if (char.isupper()):
            char = chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
        elif (char.islower()):
            char = chr((ord(char) - ord('a') + offset) % 26 + ord('a'))

        result += char
    return result


def decrypt(message, offset):
    return encrypt(message, -offset)
