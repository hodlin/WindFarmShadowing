#!/usr/bin/env python
from Turbine import Turbine
from Wind import Wind
from wind_speed import wind_speed
from math import pi, radians
import matplotlib.pyplot as plt


__author__ = 'dmytro'


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def wind_range(v0, theta0=0, theta1=90):
    for angle in drange(theta0, theta1, 1):
        yield Wind(v0, radians(angle))


w0 = Wind(speed=15, direction=0)

turbine1 = Turbine(x=0, y=0, d=40, w=w0)
turbine2 = Turbine(x=200, y=0, d=40, w=Wind(speed=15, direction=0))
turbine3 = Turbine(x=300, y=0, d=40, w=Wind(speed=15, direction=0))
turbine4 = Turbine(x=0, y=200, d=40, w=Wind(speed=15, direction=0))
turbine5 = Turbine(x=0, y=400, d=40, w=Wind(speed=15, direction=0))
turbine6 = Turbine(x=200, y=200, d=40, w=Wind(speed=15, direction=0))


turbines = [turbine1, turbine2, turbine3, turbine4, turbine5, turbine6, ]
turbines.sort()

# for turbine in turbines:
#    print turbine

theta = []
speed = [[], [], [], [], [], [], ]

output = []

for angle in drange(0, 90, 1):
    theta.append(angle)
    w0.direction = radians(angle)

    power = 0

    for i in xrange(len(turbines)):
        for j in xrange(i, len(turbines)):
            turbines[j].set_wind(wind_speed(w0, turbines[i], turbines[j]), w0.direction)

    for turbine in turbines:
        power += turbine.power

    output.append(power)

    for i in xrange(len(turbines)):
        speed[i].append(turbines[i].w.v0)


for turbine in turbines:
    print turbine


plt.figure(1)
turbines_num = len(turbines)

for i in xrange(turbines_num):
    key = '' + str(turbines_num // (turbines_num // 2)) + str(turbines_num // 2) + str(i)
    plt.subplot(key)
    plt.title('Wind speed ' + str(turbines[i]) + ', m/s')
    plt.plot(theta, speed[i], 'go') # , theta, speed[1], 'b-', theta, speed[2], 'g-', theta, speed[3], 'yo',
         # theta, speed[4], 'k-', theta, speed[5], 'c-'
    plt.axis([0, 90, 0, 20])

plt.figure(2)
plt.title('Power output, W')
plt.plot(theta, output, 'g-')
plt.axis([0, 90, 0, 100000])

plt.show()

