import sys


def decrypt():
    data = sys.stdin.read().strip()
    result = ''
    count = 0
    for elem in data:
        if elem == '.':
            count += 1
        elif count < 2:
            result += elem
            count = 0
        else:
            result = result[:-(count // 2)] + elem
            count = 0
    if result == '’':
        result = '’’'
    print(f'{data} > {result}')


if __name__ == '__main__':
    decrypt()
