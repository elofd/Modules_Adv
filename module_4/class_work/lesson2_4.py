# Реализуйте flask endpoint, принимающий на вход отсортированный массив A и число X,
# и возвращающий число из массива A, максимально близкое к числу X.
from flask import Flask, request


app = Flask(__name__)


@app.route('/close_number/', methods=['GET'])
def close_number():
    numbers = request.args.get('numbers')
    number = request.args.get('number', type=int)
    if not number or not numbers or len(numbers) < 2:
        return 'Нужно ввести массив numbers, состоящий из чисел через запятую и число number'
    try:
        numbers = sorted(list(map(int, numbers.split(','))))
        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == number:
                return f'Ближайшее число из массива {numbers} к числу {number}: {number}'
            elif numbers[mid] < number:
                left = mid + 1
            else:
                right = mid - 1
        if left == len(numbers):
            return f'Ближайшее число из массива {numbers} к числу {number}: {numbers[-1]}'

        elif abs(number - numbers[left]) < abs(number - numbers[right]):
            return f'Ближайшее число из массива {numbers} к числу {number}: {numbers[left]}'
        else:
            return f'Ближайшее число из массива {numbers} к числу {number}: {numbers[right]}'
    except ValueError:
        return 'Массив numbers должен состоять из чисел через запятую'


if __name__ == '__main__':
    app.run(debug=True)
