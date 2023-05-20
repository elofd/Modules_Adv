from datetime import datetime
import os

from flask import Flask


app = Flask(__name__)


@app.route('/get_summary_rss')
def get_summary_rss() -> str:
    summa = 0
    filename = 'output_file.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file.readlines()[1:]:
            summa += int(line.split()[5])
    result = f'<h2>Потребляемая память</h2>{summa // 1024 // 1024}МБ {summa // 1024 % 1024}КБ {summa % 1024}Б'
    return f'{result}'


@app.route('/hello_world/<string:name>')
def hello_world(name: str) -> str:
    weekday = datetime.today().weekday()
    weekdays_tuple = ('Понедельника', 'Вторника', 'Среды',
                      'Четверга', 'Пятницы', 'Субботы', 'Воскресенья')
    ending = 'его' if weekday in (0, 1, 3, 6) else "ей"
    return f'Привет, {name}. Хорош{ending} {weekdays_tuple[weekday]}!'


@app.route('/max_number/<path:numbers>')
def max_number(numbers: str) -> str:
    try:
        maximum = max(map(int, numbers.split('/')))
        return f'Максимальное число: <i>{maximum}</i>'
    except ValueError:
        return 'Ошибка, можно передавать только числа'


@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size: int, relative_path: str) -> str:
    abs_path = os.path.abspath(relative_path)
    with open(relative_path, 'r', encoding='utf-8') as file:
        data = file.read(size)
    return f'<b>{abs_path}</b> {len(data)}<br>{data}'


if __name__ == '__main__':
    app.run(debug=True)
