from flask import Flask
from random import choice
from datetime import datetime, timedelta
import os


app = Flask(__name__)
CARS = ['Chevrolet', 'Renault', 'Ford', 'Lada']
CATS = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
COUNTER = 0
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
# with open(BOOK_FILE) as book:


@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    return ', '.join(CARS)


@app.route('/cats')
def cats():
    return f'{choice(CATS)}'


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.now()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def get_random_word():
    return


@app.route('/counter')
def counter():
    global COUNTER
    COUNTER += 1
    return f'Вы посещали страницу {COUNTER} раз'