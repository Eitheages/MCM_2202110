#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from scipy.optimize import linprog # type: ignore
from mcm.data import LPdata

def solve(data: LPdata):
    target = data.c
    if target is None:
        raise KeyError("Data should contain objective function at least!")
    return linprog(target, data.A_ub, data.b_ub, data.A_eq, data.b_eq, data.bounds, method = 'simplex')

if __name__ == "__main__":

    r"""
    minimize::

        c @ x

    such that::

        A_ub @ x <= b_ub
        A_eq @ x == b_eq
        lb <= x <= ub

    Note that by default ``lb = 0`` and ``ub = None`` unless specified with
    ``bounds``.
    """

    data = LPdata(3) # dimension
    data.c = [-1, 2, 3]
    data.A_ub = [
                    [-2, 1, 1],
                    [3, -1, -2],
                ]
    data.b_ub = [
                    [9],
                    [-4],
                ]
    data.A_eq = [
                    [4, -2, -1],
                ]
    data.b_eq = [
                    [-6]
                ]
    data.bounds = [
                    [-10, None],
                    [0, None],
                    [None, None],
                ]

    res = solve(data)
    assert res.success, "Solve failure!"

    print("The minimum value of the objective function is:", res.fun)
    print("The optimal solution is:", res.x)