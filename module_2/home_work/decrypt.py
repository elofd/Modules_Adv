"""
Программа для преобразования шифрованной строки
"""

import sys


def decrypt(message: str) -> str:
    """
    Функция для преобразования зашифрованной строки
    :param message: сообщение, которое нужно преобразовать
    :return: str: расшифрованная строка
    """
    result = []
    for elem in message:
        result.append(elem)
        if len(result) > 2 and (result[-1], result[-2]) == ('.', '.'):
            result.pop()
            result.pop()
            if result:
                result.pop()
    return ''.join([elem for elem in result if elem != '.'])


def main() -> None:
    """
    Основная программа
    :return: None
    """
    data = sys.stdin.read().strip()
    print(decrypt(data))


if __name__ == '__main__':
    main()
