from sys import argv, stdin
from typing import TextIO
from os.path import isfile


def from_file(fname: str) -> list[str]:
    with open(fname, 'r') as fin:
        data = fin.readlines()
    return data


def from_stdin() -> TextIO:
    return stdin


if __name__ == '__main__':

    fnames = argv[1:]

    assert len(fnames) <= 1, f'{len(fnames)} files provided, 0 or 1 expected'

    fname = fnames[0] if len(fnames) == 1 else None

    in_data = from_file(fname) if fname != None and isfile(
        fname) else from_stdin()

    for idx, line in enumerate(in_data):
        print(f'{idx + 1}  {line}', end="")
