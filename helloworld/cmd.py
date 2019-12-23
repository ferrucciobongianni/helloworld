import argparse
from helloworld import hello_world


def cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('language', choices=['italian', 'english', 'french'])
    args = parser.parse_args()
    print(hello_world(args.language))

if __name__ == '__main__':
    cmd()
