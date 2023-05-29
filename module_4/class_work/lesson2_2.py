# Реализуйте flask endpoint, который принимает на вход массив чисел, и возвращает их сумму и произведение.
# Проверьте его работу.
from flask import Flask, request


app = Flask(__name__)


@app.route('/summa_and_multiplication/', methods=['GET'])
def summa_and_multiplication():
    numbers = request.args.get('numbers')
    try:
        numbers = list(map(int, numbers.split(',')))
        multi = 1
        for elem in numbers:
            multi *= elem
        return f'Summa {numbers} = {sum(numbers)}<br>' \
               f'Multiplication {numbers} = {multi}'
    except ValueError:
        return 'На вход ожидается массив чисел'


if __name__ == '__main__':
    app.run(debug=True)