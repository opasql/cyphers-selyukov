import random

dictionary = {
    'a': ['S', ':', 'F', 'A', 'j', '3', 'r'],
    'b': ['I', ']'],
    'c': ['a', 'o', '*'],
    'd': ['v', '7', 'Y', 's'],
    'e': ['E', 'W', 'M', 'H', 'O', 'q', 'n', 'B', '6', '=', '%'],
    'f': ['2', '?'],
    'g': ['[', '@'],
    'h': ['g', '>', 't', '$', '~', 'l'],
    'i': ['z', 'y', 'm', '<', '8'],
    'j': ['_'],
    'k': ['p'],
    'l': ['V', '(', '-', 'Z'],
    'm': ['K', 'L'],
    'n': ['|', ',', '`', 'U', '!', '.', '}'],
    'o': ['J', '\\', 'P', '{', '+', '/'],
    'p': ['9', 'D'],
    'q': ['4'],
    'r': ['k', 'X', '0', ';', 'R', ')'],
    's': ['b', 'c', "'", '5', 'Q'],
    't': ['N', 'e', 'G', 'i', 'f', 'd', 'h'],
    'u': ['1', 'C', 'u'],
    'v': ['x'],
    'w': ['&', '^'],
    'x': ['#'],
    'y': ['"', 'w'],
    'z': ['T'],
    ' ': ['ц', 'я', 'ь', 'и']
}


def encrypt(message):
    result = ''
    for symbol in message.lower():
        if symbol in dictionary:
            result += random.choice(dictionary[symbol])
    return result


def decrypt(message):
    result = ""
    for symbol in message:
        for key in dictionary:
            if symbol in dictionary[key]:
                result += key
    return result
