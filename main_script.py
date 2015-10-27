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
    for angle in drange(theta0,theta1, 1):
        yield Wind(v0, radians(angle))


w0 = Wind(15, 0, 150)

turbine1 = Turbine(x=0, y=0, d=40, w=w0, h=150)
turbine2 = Turbine(x=100, y=0, d=40, w=w0, h=150)
turbine3 = Turbine(x=0, y=100, d=40, w=w0, h=150)
turbine4 = Turbine(x=100, y=100, d=40, w=w0, h=150)

print(turbine1)
print(turbine2)
print(turbine3)
print(turbine4)

theta = []
speed1 = []
speed2 = []
speed3 = []
speed4 = []

for angle in drange(0, 90, 1):
    theta.append(angle)
    w0.direction = radians(angle)

    speed1.append(wind_speed(w0, turbine1, turbine1))
    speed2.append(wind_speed(w0, turbine1, turbine2))
    speed3.append(wind_speed(w0, turbine1, turbine3))
    speed4.append(wind_speed(w0, turbine1, turbine4))


print len(theta)
print len(speed1)
print len(speed2)
print len(speed3)
print len(speed4)

plt.figure(1)

plt.subplot(411)
plt.title(turbine1)
plt.plot(theta, speed1, 'r-')
plt.axis([0, 90, 0, 16])

plt.subplot(412)
plt.title(turbine2)
plt.plot(theta, speed2, 'b-')
plt.axis([0, 90, 0, 16])

plt.subplot(413)
plt.title(turbine3)
plt.plot(theta, speed3, 'g-')
plt.axis([0, 90, 0, 16])

plt.subplot(414)
plt.title(turbine4)
plt.plot(theta, speed4, 'y-')
plt.axis([0, 90, 0, 16])

plt.show()

w0.angle = 0
new_speed_t2 = wind_speed(w0, turbine1, turbine2)
print(new_speed_t2)