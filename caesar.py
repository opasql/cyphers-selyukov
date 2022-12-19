def encrypt(message, offset):
    result = ""

    for i in range(len(message)):
        result += chr((ord(message[i]) + offset))
    return result


def decrypt(message, offset):
    return encrypt(message, -offset)
