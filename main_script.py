#!/usr/bin/env python3
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
    for angle in drange(theta0,theta1, 1):
        yield Wind(v0, radians(angle))


w0 = Wind(15, 0, 150)

turbine1 = Turbine(x=0, y=0, d=40, w=w0, h=150)
turbine2 = Turbine(x=100, y=100, d=40, w=w0, h=150)

print(turbine1)
print(turbine2)

theta = []
speed = []

for angle in drange(0, 90, 1):
    theta.append(angle)
    w0.direction = radians(angle)
    speed.append(wind_speed(w0, turbine1, turbine2))

print(len(theta), theta)
print(len(speed), speed)

plt.plot(theta, speed)
plt.axis([0, 90, 0, 20])
plt.show()

w0.angle = 0
new_speed_t2 = wind_speed(w0, turbine1, turbine2)
print(new_speed_t2)