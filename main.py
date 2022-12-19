import caesar
import homophonic


def main_loop():
    while True:
        offset = 0
        method = int(input('1: Шифр Цезаря\n2: Омофоническая замена\n> '))
        if method == 1:
            offset = int(input('Введите сдвиг для Шифра Цезаря\n> '))
        action = int(input('1: Зашифровать\n2: Расшифровать\n> '))
        message = input('Введите сообщение\n> ')
        result = ''

        if action == 1:
            if method == 1:
                result = caesar.encrypt(message, offset)
            elif method == 2:
                result = homophonic.encrypt(message)
        elif action == 2:
            if method == 1:
                result = caesar.decrypt(message, offset)
            elif method == 2:
                result = homophonic.decrypt(message)

        print(f'Результат:\n{result}')
        print('<================>')


main_loop()
