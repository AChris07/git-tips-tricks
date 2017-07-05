import os
import sys
import subprocess
from datetime import datetime
import subscript

if __name__ == '__main__':
    name = len(sys.argv) > 1 and sys.argv[1]
    subscript.render_hello()
    print('Current time: {0}\n'.format(datetime.now()))
    print('My name is: {0}\n'.format(name) if name else 'I don\'t know your name\n')
    print('{0}\n'.format(os.getcwd()))
    print('{0}\n'.format(subprocess.check_output(['git', 'log', '--pretty=oneline']).decode('UTF-8')))
    raise Exception()
