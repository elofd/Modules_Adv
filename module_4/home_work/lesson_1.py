import os
import shlex
import subprocess

from flask import Flask, request


app = Flask(__name__)


@app.route('/uptime', methods=['GET'])
def uptime():
    UPTIME = os.popen('uptime -p').read()
    return f'Current uptime is {UPTIME}'


@app.route('/ps', methods=['GET'])
def ps():
    args: list[str] = request.args.getlist('arg')
    args_clean = [shlex.quote(elem) for elem in args]
    command_str = 'ps ' + ' '.join(args_clean)
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        return 'Something went wrong', 500

    output = result.stdout.decode()
    return f'<pre>${output}</pre>'


if __name__ == '__main__':
    app.run(debug=True)
