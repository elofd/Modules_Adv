import shlex
import subprocess


def process_count():
    command = 'ps -A'
    args = shlex.split(command)
    res = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data = res.stdout.readlines()
    return len(data) - 1


if __name__ == '__main__':
    print(process_count())
