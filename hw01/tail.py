from sys import argv, stdin
from utils import assert_valid_fnames


def handle_stdin():
    buf = []
    for line in stdin:
        if len(buf) > 17:
            buf.pop(0)

        buf.append(line)

    for line in buf:
        print(line, end='')


def handle_file(fname: str, write_title: bool = False) -> None:
    with open(fname, 'r') as fin:
        fin.seek(0, 2)
        fsize = fin.tell()
        fin.seek(max(fsize - 1024, 0), 0)
        lines = fin.readlines()[-10:]
    if write_title:
        print(f'==> {fname} <==')
    for line in lines:
        print(line, end='')
    if write_title:
        print('\n\n', end='')


if __name__ == '__main__':
    fnames = argv[1:]
    if len(fnames) == 0:
        handle_stdin()
        exit(0)

    assert_valid_fnames(fnames)
    writing_titles = len(fnames) > 1
    for fname in fnames:
        handle_file(fname, writing_titles)
