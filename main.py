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
state = 0
threshold = 47
PWert = 1.2
Abweichung = 0

SmallMotor Motor(Port.C)
myRobot.DriveBase(left_motor(Port.A), right_motor(port.B), wheel_diameter, axle_track)

def programm1():
    distanz = ds.distance()
    myRobot.drive(250)
    if distanz =< 200:
        myRobot.stop()
        myRobot.turn(120)

def programm2():
    if state == 1:
        if ts.pressed()==True:
            state=0
            myRobot.stop()
            ev3.scree.print(myRobot.distance())
        else:
            ev3.screen.clear()
            ev3.screen.print(myRobot.distance())
    else if state == 0:
        if ts.pressed()==True:
            state=1
            myRobot.reset()
            ev3.screen.clear()
            myRobot.drive(250)
        else:
            continue

def TurnRate():
    Abweichung = cs.reflection()-threshold
    turn = Abweichung * PWert
    return turn

def programm3():
    myRobot.drive(40, TurnRate())

def programm4():
    if SmallMotor.angle()==90:
        SmallMotor.run_angle(20, 90, then=Stop.HOLD)
    else:
        
