import json
from urllib.parse import unquote_plus

from flask import Flask, request


app = Flask(__name__)


@app.route('/sum', methods=['POST'])
def summa():
    array1 = request.form.getlist('array1', type=int)
    array2 = request.form.getlist('array2', type=int)

    result = ', '.join(str(elem1 + elem2) for elem1, elem2 in zip(array1, array2))

    return f'Array of sums is [{result}]'


@app.route('/sum2', methods=['POST'])
def summa2():
    form_data = request.get_data(as_text=True)
    request_data = unquote_plus(form_data)
    array = {}
    for arr in request_data.split('&'):
        key, value = arr.split('=')
        array[key] = [int(elem) for elem in value.split(',')]
    result = ', '.join(str(el_1 + el_2) for el_1, el_2 in zip(array['array1'], array['array2']))
    return f'[{result}]'


@app.route('/sum3', methods=['POST'])
def summa3_json():
    form_data = request.get_data(as_text=True)
    data_object = json.loads(form_data)
    result = ', '.join(str(el_1 + el_2) for el_1, el_2 in zip(data_object['array1'], data_object['array2']))
    return f'[{result}]'


if __name__ == '__main__':
    app.run(debug=True)
