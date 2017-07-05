import os
import sys
from datetime import datetime

if __name__ == '__main__':
    name = len(sys.argv) > 1 and sys.argv[1]
    print 'Maybe not'
    print 'Current time: {0}'.format(datetime.now())
    print 'My name is: {0}'.format(name) if name else 'I don\'t know your name'
    print os.getcwd()
    raise Exception()
