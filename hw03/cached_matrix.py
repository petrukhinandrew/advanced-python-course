from functools import reduce
from operator import xor
from base_matrix import BaseMatrix


class MatrixHashMixin:
    def __hash__(self) -> int:
        # element wise xor
        return reduce(xor, [reduce(xor, line, 0) for line in self.value()], 0)


class HashableMatrix(MatrixHashMixin, BaseMatrix):
    _cache = {}

    def __matmul__(self, other) -> BaseMatrix:
        lhsc = hash(self)
        rhsc = hash(other)
        k = (lhsc, rhsc)
        if (cached := HashableMatrix._cache.get(k)) != None:
            return cached
        HashableMatrix._cache[k] = HashableMatrix(
            super().__matmul__(other).value())
        return HashableMatrix._cache[k]
