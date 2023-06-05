import subprocess

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange


app = Flask(__name__)


class RemoteUploadForm(FlaskForm):
    command = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired(), NumberRange(min=0, max=30)])


@app.route('/remote_upload', methods=['POST'])
def remote_upload():
    form = RemoteUploadForm()

    if form.validate_on_submit():
        command = f'prlimit --nproc=1:1 python -c {form.command.data}'
        with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
            try:
                outs, errs = proc.communicate(timeout=form.timeout.data)
                if errs:
                    return f'{errs}', 400
                else:
                    return f'{outs}', 200
            except subprocess.TimeoutExpired:
                return 'Execution timed out', 400
    return f"Invalid input, {form.errors}", 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
