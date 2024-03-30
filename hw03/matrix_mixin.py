import numpy as np 
from numpy.lib.mixins import NDArrayOperatorsMixin as OpMixin

class MatrixMixin:
    def __init__(self, matrix) -> None:
        self._matrix = matrix

    @property
    def matrix(self):
        return self._matrix
    
    @matrix.setter
    def matrix(self, value):
        if not isinstance(value, np.ndarray) and not (isinstance(value, list) and isinstance(value[0], list)):
            raise ValueError("unsupported input type {}".format(value))
        self._matrix = value
    
    def save_as(self, fname: str) -> None:
        np.savetxt(fname, self.matrix, fmt="%s")
    
    def __str__(self) -> str:
        return "\n".join(map(str, self._matrix))

class MixedMatrix(OpMixin, MatrixMixin):

    _HANDLED_TYPES = (np.ndarray, list)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MixedMatrix,)):
                raise NotImplemented
        inputs = list(x._matrix if isinstance(x, MixedMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = list(
                x._matrix if isinstance(x, MixedMatrix) else x
                for x in out)

        if method == '__call__':
            return MixedMatrix(np.asarray(getattr(ufunc, method)(*inputs, **kwargs)).tolist())
        else:
            raise NotImplemented