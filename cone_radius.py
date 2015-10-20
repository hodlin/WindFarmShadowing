#!/usr/bin/env python3
from Turbine import Turbine
from cone_height import cone_height
from math import tan, radians

__author__ = 'dmytro'


def cone_radius(t1=Turbine(0, 0, 0), t2=Turbine(0, 0, 0)):
    """
    Diameter of wind flow cone at the second turbine
    :param t1: first turbine
    :param t2: second turbine
    :return: diameter in [meters]
    """
    return round(t1.d / 2 + cone_height(t1, t2) * tan(radians(4.5)), 1)


if __name__ == "__main__":
    pass