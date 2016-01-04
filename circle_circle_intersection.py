#!/usr/bin/env python
from math import acos, fabs, sqrt, pi


def circle_intersection_area(r1=0, r2=0, d=0):
    """
    Intersection of two circles
    :param r1: radius of first circle in [meters]
    :param r2: radius of second circle in [meters]
    :param d: distance between centers of two circles in [meters]
    :return: area of lens  in which the circles intersect in [square meters]
    """
    assert r1 >= 0 and r2 >= 0, "Radiuses could not be negative! r1:{r1:2.2f} r2:{r2:2.2f}".format(r1=r1, r2=r2)

    assert d >= 0, "Distance could not be negative! d:{d:3.1f}".format(d=d)

    if d > r1 + r2:
        return 0

    if fabs(r1 - r2) >= d:
        area = pi * min(r1, r2)**2
        return round(area, 2)

    d1 = (d**2 - r2**2 + r1**2) / (2 * d)
    d2 = (d**2 + r2**2 - r1**2) / (2 * d)

    area = r2**2 * acos(d2 / r2)\
                + r1**2 * acos(d1 / r1)\
                - 0.5 * sqrt((-d + r2+ r1) * (d + r2 - r1) * (d - r2 + r1) * (d + r2 + r1))

    return round(area, 2)


if __name__ == "__main__":

    r1 = float(input("Raudius of first circle, m: "))
    r2 = float(input("Raudius of second circle, m: "))
    d = float(input("Distance between circles, m: "))

    area = circle_intersection_area(r1, r2, d)

    print("Area of intersection: " + str(area))
