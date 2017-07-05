from pyfiglet import figlet_format

def render_hello():
    print(figlet_format('Hello World!', font='starwars'))

if __name__ == '__main__':
    render_hello()