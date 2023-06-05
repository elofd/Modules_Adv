import shlex
import subprocess
import time


def main():
    start = time.time()
    command = 'sleep 15 && echo My mission is done here!'.split('&&')
    args_1 = shlex.split(command[0])
    args_2 = shlex.split(command[1])
    procs = []

    for i in range(10):
        p = subprocess.Popen(args_1)
        procs.append(p)

    for proc in procs:
        proc.wait()
        p_2 = subprocess.Popen(args_2)

    print(f'Done in {time.time() - start}')


if __name__ == '__main__':
    main()
