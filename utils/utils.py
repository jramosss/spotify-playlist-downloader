RED = '\033[91m'
GREEN = '\033[92m'
CLEAN = '\033[39m'


def clean():
    print(CLEAN)


def print_in_red(msg):
    print(RED + msg)
    clean()


def print_in_green(msg):
    print(GREEN + msg)
    clean()
