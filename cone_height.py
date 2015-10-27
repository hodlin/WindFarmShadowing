#!/usr/bin/env python3
from Turbine import Turbine
from math import cos

__author__ = 'dmytro'


def cone_height(t1=Turbine(0, 0, 20), t2=Turbine(0, 0, 20)):
    """
    Calculating "height" of wint stream cone from first turbine to the plane of second
    :param t1: first turbine
    :param t2: second turbine
    :return: distance in [meters]
    """
    d = t1.dist(t2)
    direct = t1.direction(t2)
    theta = t1.w.direction

    if theta == 0 or theta == direct:
        return d * cos(direct)

    if theta > direct:
        return d * cos(theta - direct)

    if theta < direct:
        return d / cos(direct - theta)


if __name__ == "__main__":
    pass