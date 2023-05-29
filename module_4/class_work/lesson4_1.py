from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field
from wtforms.validators import InputRequired, Email, NumberRange, ValidationError


def number_length(min: int, max: int, message: str | None = None):

    def wrapped_func(form: FlaskForm, field: Field):
        if field.data < min or field.data > max:
            raise ValidationError

    return wrapped_func


class NumberLength:

    def __call__(self, form: FlaskForm, field: Field):
        if field.data < 10 ** 9 or field.data > 10 ** 10 - 1:
            raise ValidationError


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), number_length(min=10 ** 9, max=10 ** 10 - 1, message='ERROR')])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


class TicketForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    family_name = StringField(validators=[InputRequired()])
    number = StringField(validators=[InputRequired(), NumberRange(min=10 ** 6, max=10 ** 7 - 1)])


app = Flask(__name__)


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        return f'Successfully registered user {email} with phone +7{phone}'

    return f'Invalid input, {form.errors}', 400


@app.route('/ticket', methods=['POST'])
def ticket():
    form = TicketForm()
    number = form.number.data
    if form.validate_on_submit() and number.isdigit() and not number.startswith('0') and len(number) == 6:
        if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
            return f'Поздравляем вас, {form.name.data} {form.family_name.data}'
        return '"Неудача. Попробуйте ещё раз!"'
    return f'Invalid input, {form.errors}', 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
