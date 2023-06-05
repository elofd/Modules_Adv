import shlex
import subprocess
from os import kill
from time import sleep

from flask import Flask


app = Flask(__name__)


def app_run(port: int) -> None:
    try:
        app.run(port=port)
    except:
        command = shlex.split('lsof -i:5000')
        res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pid = res.stdout.decode().split('\n')[1].split()[1]
        print(f'ERROR, TRYING CLOSE PORT {pid}...')
        kill(int(pid), 9)
        sleep(5)
        print('DONE')
        print(f'RUN APP')
        app_run(port)


if __name__ == '__main__':
    app_run(5000)
