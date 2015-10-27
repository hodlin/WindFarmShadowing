#!/usr/bin/env python
from Wind import Wind
from Turbine import Turbine
from circle_circle_intersection import circle_intersection_area
from cone_radius import cone_radius
from distance_between_circles import distance_between_circles

__author__ = 'dmytro'


def wind_speed(w0=Wind(), t1=Turbine(0, 0, 0), t2=Turbine(0, 0, 0)):
    """
    Calculate wind speed at second turbine
    :param t1: first turbine
    :param t2: second turbine
    :return:speed in [meters per second]
    """
    t_dist = t1.dist(t2)
    r_radius = t1.d / 2
    c_radius = cone_radius(t1, t2)
    c_dist = distance_between_circles(t1, t2)

    try:
        in_area = circle_intersection_area(r_radius, c_radius, c_dist)
    except AssertionError:
        in_area = 0

    w_speed = w0.v0 * (in_area / t1.area)\
                * (1 - (1 - (t1.w.v0 / (3 * w0.v0)))\
                * (r_radius / (r_radius + 0.078 * t_dist))**2)\
                + w0.v0 * ((t1.area - in_area) / t1.area)

    return round(w_speed, 2)


if __name__ == "__main__":
    pass