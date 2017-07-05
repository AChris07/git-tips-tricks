import sys
import subprocess
from datetime import datetime
from colorama import init, Fore
init(autoreset=True)

if __name__ == '__main__':
    name = len(sys.argv) > 1 and sys.argv[1]
    print('More changes!')
    print('Current time: {1}{0}'.format(datetime.now(), Fore.YELLOW))
    print('My name is: {1}{0}'.format(name, Fore.CYAN) if name else 'I don\'t know your name')
    print('Current branch is {1}{0}'.format(subprocess.check_output(['git', 'symbolic-ref', 'HEAD', '--short']).decode('UTF-8'), Fore.RED))
