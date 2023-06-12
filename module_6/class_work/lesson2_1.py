import logging

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired


app = Flask(__name__)

logger = logging.getLogger('divider')


class DivideForm(FlaskForm):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])


@app.route('/divide', methods=['POST'])
def divide():
    form = DivideForm()

    if form.validate_on_submit():
        a, b = form.a.data, form.b.data
        logger.debug(f'Form is valid. a = {a}, b = {b}')
        return f'a / b = {a / b:.2f}\n'

    logger.error(f'Form not valid, error = {form.errors}')
    return f'Bad request. Error = {form.errors}\n', 400


@app.errorhandler(ZeroDivisionError)
def handle_exception(error: ZeroDivisionError):
    logger.exception('We are unable to divine by zero!', exc_info=error)
    return 'We are unable to divine by zero!\n', 400


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('Started divider server')
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
