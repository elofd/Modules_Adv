import os
from typing import List


def get_tuple_of_words_for_t9(path: str = os.path.abspath('/usr/share/dict/words')) -> tuple:
    with open(path, 'r') as file_with_words:
        words_for_t9 = tuple(map(lambda word: word.lower(),
                                 filter(lambda word: word.isalpha(), file_with_words.read().split('\n'))))
    return words_for_t9


def t9_sym(dig: int) -> tuple:
    if dig == 2:
        return 'a', 'b', 'c', ''
    if dig == 3:
        return 'd', 'e', 'f', ''
    if dig == 4:
        return 'g', 'h', 'i', ''
    if dig == 5:
        return 'j', 'k', 'l', ''
    if dig == 6:
        return 'm', 'n', 'o', ''
    if dig == 7:
        return 'p', 'q', 'r', 's'
    if dig == 8:
        return 't', 'u', 'v', ''
    if dig == 9:
        return 'w', 'x', 'y', 'z'


def my_t9(input_numbers: str) -> List[str]:
    words_for_t9 = get_tuple_of_words_for_t9()
    old_words = words_for_t9
    for position, dig in enumerate(input_numbers):
        next_words_for_t9 = filter(
            lambda sym:
            ((len(sym) > position) and (sym[position] == t9_sym(int(dig))[0])) or
            ((len(sym) > position) and (sym[position] == t9_sym(int(dig))[1])) or
            ((len(sym) > position) and (sym[position] == t9_sym(int(dig))[2])) or
            ((len(sym) > position) and (sym[position] == t9_sym(int(dig))[3])),

            old_words
        )
        old_words = tuple(next_words_for_t9)

    result = filter(lambda sym: len(sym) == len(input_numbers), old_words)
    return list(result)


if __name__ == '__main__':
    numbers: str = input('Введите последовательность цифр: ')
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
