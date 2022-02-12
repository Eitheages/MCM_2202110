#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from typing import Tuple
import cvxpy as cp # type: ignore
from mcm.data import IPdata
from numpy import array

def solve(data: IPdata) -> Tuple[cp.Problem, cp.Variable]:
    assert 'ECOS_BB' in cp.installed_solvers(), "haven't installed ECOS_BB"
    x = cp.Variable(data.dimen, integer = True)
    obj = cp.Minimize(data.c * x)
    cons = [data.A_ub * x <= data.b_ub, x >= 0] # change when necessary
    prob = cp.Problem(obj, cons)
    prob.solve(solver = 'ECOS_BB', verbose = False)
    return prob, x

if __name__ == '__main__':

    r"""
    minimize::

        c @ x

    such that::

        A_ub @ x <= b_ub
        A_eq @ x == b_eq
        x >= 0

    Constraints can be appended by editing function 'solve'
    """

    data = IPdata(2) # dimension
    data.c = [40, 90]
    data.A_ub = [
                    [9, 7],
                    [-7, -20],
                ]
    data.b_ub = [56, -70] # need a column vector

    res = solve(data)
    print('\n\n', res[0].status)

    print("The minimum value of the objective function is:", res[0].value)
    print("The optimal solution is:", res[1].value)