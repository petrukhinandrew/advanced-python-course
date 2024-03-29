from __future__ import annotations


class BaseMatrix:
    def __init__(self, data: list[list[int]]) -> None:
        self.__data = data

    def value(self) -> list[list[int]]:
        return self.__data

    def __str__(self) -> str:
        return "\n".join(map(str, self.__data))

    def __add__(self, other: BaseMatrix) -> BaseMatrix:
        self.__same_dim(other)
        return self.__elemwise_op(other, lambda x, y: x + y)

    def __mul__(self, other: BaseMatrix) -> BaseMatrix:
        self.__same_dim(other)
        return self.__elemwise_op(other, lambda x, y: x * y)

    def __elemwise_op(self, other: BaseMatrix, el_f: function) -> BaseMatrix:
        n, m = len(self.__data), len(self.__data[0])
        new_data = [[el_f(self.__data[i][j], other.__data[i][j])
                     for j in range(m)] for i in range(n)]
        return BaseMatrix(new_data)

    def __matmul__(self, other: BaseMatrix) -> BaseMatrix:
        self.__allow_mat_mul(other)
        dh, dw = len(self.__data), len(other.__data[0])

        new_data = [[sum(self.__data[i][k] * other.__data[k][j] for k in range(len(self.__data[0])))
                     for j in range(dw)] for i in range(dh)]
        return BaseMatrix(new_data)

    def __same_dim(self, other: BaseMatrix) -> None:
        BaseMatrix.__throw_if_invalid(other)
        BaseMatrix.__throw_if_invalid(self)
        d1, d2 = len(self.__data), len(self.__data[0])
        if d1 != len(other.__data):
            raise ValueError("bad fst dim")
        if d2 != len(other.__data[0]):
            raise ValueError("bad snd dim")

    def __allow_mat_mul(self, other: BaseMatrix) -> None:
        BaseMatrix.__throw_if_invalid(other)
        BaseMatrix.__throw_if_invalid(self)
        d = len(self.__data[0])
        od = len(other.__data)
        if d != od:
            raise ValueError("bad mat dimensions")

    def __throw_if_invalid(mat: BaseMatrix) -> None:
        if mat.__data is None:
            raise ValueError("mat is None")
        if len(mat.__data) <= 0:
            raise ValueError("mat cannot be empty")
        n = len(mat.__data[0])
        if not all([len(x) == n for x in mat.__data]):
            raise ValueError("bad mat size")
