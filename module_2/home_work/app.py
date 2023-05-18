import subprocess

from flask import Flask


app = Flask(__name__)


@app.route('/get_summary_rss')
def get_summary_rss():
    summa = 0
    filename = 'output_file.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file.readlines()[1:]:
            summa += int(line.split()[5])
    result = f'<h2>Потребляемая память</h2>{summa // 1024}КБ {summa % 1024}Б'
    return f'{result}'


if __name__ == '__main__':
    app.run(debug=True)