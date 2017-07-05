import os
import sys
import subprocess
from datetime import datetime

if __name__ == '__main__':
    name = len(sys.argv) > 1 and sys.argv[1]
    print 'Cool stuff!\n'
    print 'Current time: {0}\n'.format(datetime.now())
    print 'My name is: {0}\n'.format(name) if name else 'I don\'t know your name\n'
    print '{0}\n'.format(os.getcwd())
    print '{0}\n'.format(subprocess.check_output(['git', 'log', '--pretty=oneline']))
    raise Exception()
