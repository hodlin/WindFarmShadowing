#!/usr/bin/env python3
from math import radians
from Turbine import Turbine
from Wind import Wind
from wind_speed import wind_speed
import matplotlib.pyplot as plt

class Farm:
    """
    Farm consists of a number of wind turbines and provide energetic calculations
    """

    def __init__(self, site,  wind_speed=0, turbine_rotor_diameter=0, layout='rectangle'):
        """
        Constructing a farm

        :param site: site for wind farm
        :param wind_speed: wind object to apply to a farm
        :param turbine_rotor_diameter: turbine object to apply to a farm
        :param layout: layout scheme whether 'rectangle' or 'checkerboard'
        :return:
        """
        # assert (site.__reduce__(lambda i, j: i+j) > 0,
        #         "Senseless site - height: {h}, width: {w}".format(h=site[0], w=site[1]))
        # assert (turbine.d > 0,
        #         "Senseless turbine - diameter is {d}".format(d=turbine.d))
        # assert (wind.v0 > 0,
        #         "Senseless wind - speed: {w}".format(w=wind.v0))
        # assert (layout in ('rectangle', 'checkerboard'),
        #         "Can't resolve layout: '{l}'".format(l=layout))

        self.site = site
        self.wind = Wind(wind_speed, 0)
        self.wind_speed = wind_speed
        self.turbine_rotor_diameter = turbine_rotor_diameter
        self.layout = layout
        self.turbines = []

    def turbines_list(self, x, y):
        """
        Creating a list of specified number of turbines

        :param x: number of turbines in x-direction
        :param y: number of turbines in y-direction
        :return:
        """
        self.turbines = []

        distance_x = self.site[0] / x + 1
        distance_y = self.site[1] / y + 1

        for i in range(x):
            for j in range(y):
                self.turbines.append(Turbine(d=self.turbine_rotor_diameter,
                                             x=i*distance_x, y=j*distance_y, w=Wind(self.wind_speed, 0)))
        self.turbines.sort()

        return None

    def power_shape(self, config=(0, 0), step=1, average=True):
        """
        Create a generator on farm output layout

        NOTICE:
        x-distance and y-distance should be => self.turbine_diameter

        :param step: step in degrees
        :param config: tuple of type (number of turbines in x-direction,... y-direction)
        :param average: bool whether return integral value or sequence
        :return:
        """
        # assert ((config[0] > self.turbine_diameter) & (config[1] > self.turbine_diameter),
        #         'Distance between turbines x: {a}, y: {b} should be grater than radius r: {c}'
        #         .format(a=config[0], b=config[1], c=self.turbine_diameter / 2))

        self.turbines_list(config[0], config[1])
        theta = []
        output = []

        for angle in range(0, 91, step):
            theta.append(angle)
            self.wind.direction = radians(angle)

            power = 0

            for i in xrange(len(self.turbines)):
                self.turbines[i].w.set_direction(self.wind.direction)
                for j in xrange(i+1, len(self.turbines)):
                    self.turbines[j].set_wind(wind_speed(self.wind, self.turbines[i], self.turbines[j]),
                                              self.wind.direction)

            for turbine in self.turbines:
                power += round(turbine.power, 2)

            output.append(power)

        if average:
            return sum(output) / len(self.turbines)  #__reduce__(lambda x, y: x+y/len(self.turbines))

        return [theta, output]

    def optimise(self, optimise_by_x=False, optimise_by_y=False):
        """
        Optimisation routine

        :param optimise_by_x: whether change x distance
        :param optimise_by_y: whether change y distance
        :return: tuple of optimal (x-distance, y-distance)
        """
        # assert (not optimise_by_x or not optimise_by_y,
        #         'You should specify whether optimise by x or y distance or both')

        stop_x = False
        stop_y = False

        width_x, width_y = self.site
        x_dir_num = width_x / self.turbine_rotor_diameter + 1
        y_dir_num = width_y / self.turbine_rotor_diameter + 1

        initial = [x_dir_num, y_dir_num]
        step = 1
        current_spacing = initial
        best_spacing = initial
        best_output = 0

        # realise boundary search for optimal solution !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        while True:
            current_output = self.power_shape(config=tuple(current_spacing))
            print('Output of farm with spacing {0} is {1}'.format(current_spacing, current_output))
            print('Number of turbines: {}'.format(len(self.turbines)))
            print('----------------------------------------------------------------')

            if current_output > best_output:
                best_output = current_output
                best_spacing = current_spacing[:]

            if optimise_by_x and current_spacing[0] > 2:
                current_spacing[0] -= step
            else:
                stop_x = True

            if optimise_by_y and current_spacing[1] > 2:
                current_spacing[1] -= step
            else:
                stop_y = True

            if stop_x and stop_y:
                break

        return best_spacing, best_output

    def visualise(self, generator):
        pass

if __name__ == '__main__':

    site = (200, 200)
    farm = Farm(site, 15, 40)
    best_spacing, best_output = farm.optimise(optimise_by_x=True, optimise_by_y=True)
    print('*' * 30)
    print('Site sizes: {}'.format(site))
    print('Best spacing: {}'.format(best_spacing))
    print('Best output: {}'.format(best_output))
    print('*' * 30)

    # ut_shape = farm.power_shape(best_spacing, average=False)
    #
    # plt.figure(1)
    # plt.title('Power output')
    # plt.plot(output_shape[0], output_shape[1], 'k-', linewidth=2)
    # plt.xlabel('Wind direction, deg')
    # plt.ylabel('Output, kW')
    # plt.axis([0, 90, 0, 10000])
