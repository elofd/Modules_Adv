import subprocess
import shlex
import json


def run_program():
    res = subprocess.run(['python', 'test_program.py'], input=b'some input\nother input',
                         stderr=subprocess.STDOUT)
    print(res)


def run_command():
    command = 'curl -i -H "Accept: application/json" -X GET https://api.ipify.org?format=json'
    args = shlex.split(command)
    res = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data = res.stdout.decode().split()
    ip = json.loads(data[-1])
    return ip['ip']


def process_count():
    command = 'ps -A'
    args = shlex.split(command)
    res = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data = res.stdout.decode().split('\n')[1:-1]
    return len(data)


if __name__ == '__main__':
    process_count()