#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
ds=DistantSensor(Port.S1)
cs=ColorSensor(Port.S2)
ts=TouchSensor(Port.S3)

myRobot.DriveBase(left_motor(Port.A), right_motor(port.B), wheel_diameter, axle_track)

def programm1():
    distanz = ds.distance()
    myrobot.drive(250)
    if distanz =< 200:
        myrobot.stop()
        myrobot.turn(120)

def programm2():
    if button == False:
        if ts.pressed=True:
            button = True
    if button == True:
        if ts.pressed = True:
            button = False