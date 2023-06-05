import subprocess
import time


def run_program():
    start = time.time()
    procs = []
    for p_num in range(1, 6):
        p = subprocess.Popen(
            ['python', 'test_program.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print(f'Process num {p_num} started. PID: {p.pid}')
        procs.append(p)

    for proc in procs:
        proc.wait()
        if b'Done' in proc.stdout.read() and proc.returncode == 0:
            print(f'Process with PID {proc.pid} ended successfully')
    print(f'Done in {time.time() - start}')


if __name__ == '__main__':
    run_program()
