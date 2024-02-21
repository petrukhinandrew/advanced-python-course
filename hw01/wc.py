from sys import argv, stdin
from typing import TextIO
from utils import assert_valid_fnames, tuple_elemwise_sum, tuple_as_string


def __wc(src: list[str] | TextIO) -> tuple[int, int, int]:
    lines, words, letters = 0, 0, 0
    for line in src:
        lines += 1
        words += len(line.split())
        letters += len(line)
    return (lines, words, letters)


def wc_file(fname: str) -> tuple[int, int, int]:
    with open(fname, 'r') as src:
        return __wc(src)


def wc_stdin() -> tuple[int, int, int]:
    return __wc(stdin)


if __name__ == '__main__':

    if len(argv) == 1:
        print(tuple_as_string(wc_stdin()))
        exit(0)

    fnames = argv[1:]
    assert_valid_fnames(fnames)
    is_writing_total, total = len(fnames) > 1, (0, 0, 0)

    for fname in fnames:
        cur_file_wc = wc_file(fname)

        print(f"{tuple_as_string(cur_file_wc)} {fname}")

        total = tuple_elemwise_sum(total, cur_file_wc)

    if is_writing_total:
        print(f'{tuple_as_string(total)} total', end='')
