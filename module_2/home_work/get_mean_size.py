import sys


def get_mean_size():
    data = sys.stdin.readlines()[1:]
    sizes = [int(line.split()[4]) for line in data if len(line.split()) > 4]
    if sizes:
        summa = sum(sizes) / len(sizes)
        print(f'Средний размер файла равен: {summa}')
    else:
        print('Файлов и их размеров не найдено')


if __name__ == '__main__':
    get_mean_size()