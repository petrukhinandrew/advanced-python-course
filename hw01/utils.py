from os.path import isfile


def assert_valid_fnames(fnames: list[str]) -> bool:
    for fname in fnames:
        assert isfile(fname), f"expected file, got {fname}"


def tuple_elemwise_sum(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return (x[0] + x[1] for x in zip(a, b))


def tuple_as_string(t: tuple[int]) -> str:
    return ' '.join(map(str, t))
