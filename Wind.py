#!/usr/bin/env python3
from math import pi

__author__ = 'dmytro'


class Wind(object):
    """
    Representation of wind
    Consists of:
    initial speed v0 in [meters per second]
    direction in [radians]
    height at wich speed initialized [meters]
    Constraints:
    v0 = (0, 50)
    direction = (0, pi)
    height = (10, 200)
    """
    def __init__(self, speed=0, direction=0, height=10):
        """
        Initialize wind parameters
        :param speed: initial speed in [meters per second]
        :param direction: direction (tangents of angle) in [radians]
        :param height: height of
        :return:
        """
        if 0 <= speed <= 50:
            self.v0 = speed
        else:
            raise ValueError("Out of range value of initial velocity")
        if 0 <= direction <= pi:
            self.direction = direction
        else:
            raise ValueError("Out of range value of direction")
        if 10 <= height <= 200:
            self.height = height
        else:
            raise ValueError("Out of range value of height")


    def get_speed(self, h = 0):
        """
        Calculate value of wind speed at h height
        :param h: height in [meters]
        :return: speed of wind in [meters per second]
        """
        pass


if __name__ == "__main__":
    pass
