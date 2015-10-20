#!/usr/bin/env python3
from Turbine import Turbine
from math import sin, tan

__author__ = 'dmytro'


def distance_between_circles(t1=Turbine(0, 0, 20), t2=Turbine(0, 0, 20)):
    """
    Calculating distance between direction of wind stream and second turbine
    :param t1: first turbine
    :param t2: second turbine
    :return: distance in [meters]
    """
    d = t1.dist(t2)
    direct = t1.direction(t2)
    theta = t1.w.direction

    if theta == 0:
        return d * sin(direct)

    if theta > direct:
        return d * sin(theta - direct)

    if theta < direct:
        return d * tan(direct - theta)


if __name__ == "__main__":
    pass