def encrypt(message, offset):
    """Прибавляет offset к Unicode code point каждого элемента message"""
    result = ""

    for i in range(len(message)):
        result += chr((ord(message[i]) + offset))
    return result


def decrypt(message, offset):
    """Вызывает encrypt с отрицательным offset"""
    return encrypt(message, -offset)
