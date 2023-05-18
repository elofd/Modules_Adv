import datetime
from flask import Flask


app = Flask(__name__)
COUNTER = 0


@app.route('/hello')
def test_function():
    return 'Это новая тестовая страничка, ответ сгенерирован в %s' % datetime.datetime.now().utcnow()


@app.route('/hello/world')
def hello_world():
    return 'Привет, Мир!'


@app.route('/counter')
def counter():
    global COUNTER
    COUNTER += 1
    return f'Страница открывалась: {COUNTER} раз'

