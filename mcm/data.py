from typing import List, TypeVar
import numpy as np

Number = TypeVar("Number", int, float, None)

class _Matrix:

    @staticmethod
    def check(content):
        for row in content:
            for ele in row:
                if not isinstance(ele, (int, float)):
                    raise TypeError("Invalid input: only number is accepted in a matrix!")

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, val: List[List[Number]]):
        if val is None:
            instance.__dict__[self.name] = None
        else:
            _Matrix.check(val)
            instance.__dict__[self.name] = np.array(val)

class Data:
    pass

class LPdata(Data):

    A_ub = _Matrix('A_ub'); b_ub = _Matrix('b_ub')
    A_eq = _Matrix('A_eq'); b_eq = _Matrix('b_eq')

    def __init__(self, x: int):
        self._cnt = x

    @property
    def bounds(self):
        return self._bounds

    @bounds.setter
    def bounds(self, val: List[List[Number]]):
        for single in val:
            if len(single) != 2:
                raise TypeError("Tuple in bounds must have two arguments!")
            for ele in single:
                if ele is not None and not isinstance(ele, (int, float)):
                    raise TypeError("Invalid input: only number or None is accepted in 'bounds'!")

        self._bounds = np.array(val)

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, val: List[Number]):
        for ele in val:
            if not isinstance(ele, (int, float)):
                raise TypeError("Invalid input: only number is accepted in row vector 'c'")

        self._c = np.array(val)