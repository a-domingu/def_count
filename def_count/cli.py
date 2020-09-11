import click
import sys, os
from def_count import get_files, count


def main():
    ls_directories = sys.argv[1:]
    i = 1
    for directory in ls_directories:
        path = os.path.join(os.getcwd(), directory)
        ls_files = get_files(path)
        num = count(ls_files)
        print(f'{i}: {directory} -- {num} instances of \'def\'')
        i += 1

if __name__ == '__main__':
    main()