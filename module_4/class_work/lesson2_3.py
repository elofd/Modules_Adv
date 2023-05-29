# Реализуйте flask endpoint, который принимает на вход 2 массива A и B и возвращает
# все возможные комбинации пар чисел a и b, где a — число из массива A, а b — число из массива B.
from flask import Flask, request


app = Flask(__name__)


@app.route('/combinations/', methods=['GET'])
def combinations():
    numbers_a = request.args.get('numbers_a')
    numbers_b = request.args.get('numbers_b')
    if not numbers_a or not numbers_b:
        return 'Нужно ввести 2 массива, numbers_a и numbers_b'
    try:
        numbers_a = list(map(int, numbers_a.split(',')))
        numbers_b = list(map(int, numbers_b.split(',')))
        result = []
        for i_elem in numbers_a:
            for j_elem in numbers_b:
                result.append((i_elem, j_elem))
        return f'Все возможные комбинации массивов {numbers_a} и {numbers_b}:<br>{result}'
    except ValueError:
        return 'Элементами массивов могут быть только числа'


if __name__ == '__main__':
    app.run(debug=True)
