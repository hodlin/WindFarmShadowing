#!/usr/bin/env python
from collections.abc import MutableSet

__author__ = 'dmytro'


class Farm(MutableSet):
    """
    Farm consists of a number of wind turbines and provide energetic calculations
    """
    turbines = []

    def __init__(self, iterable):
        """

        :param iterable:
        :return:
        """