import os

from flask import Flask


app = Flask(__name__)


@app.route('/hello/<username>')
def hello(username) -> str:
    return f'Hello, {username}!'


@app.route('/even/<int:number>')
def even(number) -> str:
    return f'Число {number} <b>четное</b>' if number % 2 == 0 else f'Число {number} <b>нечётное</b>'


@app.route('/compare/<float:number_1>/<float:number_2>')
def compare(number_1, number_2) -> str:
    if number_1 == number_2:
        sign = '='
    elif number_1 > number_2:
        sign = '>'
    else:
        sign = '<'
    return f'{number_1} {sign} {number_2}'


@app.route('/check_exists/<path:file_path>')
def check_exists(file_path):
    """
    Check if file exists on file system
    :param file_path: path to file to be checked
    :return: http response
    """
    file_exists = os.path.exists(file_path)
    response_code = 200 if file_exists else 404
    result = 'exists' if file_exists else 'not exists'
    return f'file <h2>{file_path}</h2> {result}', response_code


if __name__ == '__main__':
    app.run(debug=True)