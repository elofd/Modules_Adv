from flask import Flask


app = Flask(__name__)
storage = {}


@app.route('/add/<date>/<int:expense>')
def add(date: str, expense: int) -> str:
    try:
        if len(date) != 8 and int(date):
            raise ValueError
        storage.setdefault(int(date[:4]), {}).setdefault(int(date[4:6]), 0)
        storage[int(date[:4])][int(date[4:6])] += expense
        return f'{storage}'
    except ValueError:
        return 'Дата введена некорректно'


@app.route('/calculate/<int:year>')
def calculate_year(year: int) -> str:
    try:
        total = sum(storage[year].values())
        return f'Суммарные траты за {year} год: {total}'
    except KeyError:
        return f'Суммарные траты за {year} год: 0'


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year: int, month: int) -> str:
    try:
        total = storage[year][month]
        return f'Суммарные траты за {month} месяц {year} года: {total}'
    except KeyError:
        return f'Суммарные траты за {month} месяц {year} года: 0'


if __name__ == '__main__':
    app.run(debug=True)