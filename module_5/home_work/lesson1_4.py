import sys
from traceback import format_exc


class Redirect:

    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        if self.stdout:
            self.old_stdout = sys.stdout
            sys.stdout = self.stdout
        if self.stderr:
            self.old_stderr = sys.stderr
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_value, traceback):
        if self.stdout:
            sys.stdout = self.old_stdout
        if self.stderr:
            sys.stderr.write(format_exc())
            sys.stderr = self.old_stderr
        return True


print('Hello stdout')
stdout_file = open('stdout.txt', 'w')
stderr_file = open('stderr.txt', 'w')

with Redirect(stdout=stdout_file, stderr=stderr_file):
    print('Hello stdout.txt')
    raise Exception('Hello stderr.txt')

print('Hello stdout again')
raise Exception('Hello stderr')
