#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
ds=UltrasonicSensor(Port.S4)
cs=ColorSensor(Port.S3)
ts=TouchSensor(Port.S2)
SmallMotor=Motor(Port.C, positive_direction=Direction.CLOCKWISE)

state = 0
Programm = 0
threshold = 47
PWert = 1.2
Abweichung = 0
myRobot = DriveBase(Motor(Port.A), Motor(Port.B), 46, 200)


def TurnRate():
    Abweichung = cs.reflection()-threshold
    turn = Abweichung * PWert
    return turn

def Quadrat():
    myRobot.turn(90)
    for i in range (2):
        myRobot.straight(400)
        myRobot.turn(90)
    myRobot.straight(400)
    i = 0

def Drehung():
    myRobot.straight(-50)
    myRobot.turn(360)
    myRobot.straight(50)

def Dreieck():
    myRobot.turn(150)
    for x in range(1):
        myRobot.straight(400)
        myRobot.turn(120)
    myRobot.straight(400)
    myRobot.turn(-30)
    x = 0

#Abstandsregelung
def programm1():
    distanz = ds.distance()
    myRobot.drive(250)
    if distanz <= 200:
        myRobot.stop()
        myRobot.turn(120)

#Distanz Messung
def programm2():
    if state == 1:
        if ts.pressed()==True:
            state=0
            myRobot.stop()
            ev3.screen.print(myRobot.distance())
        else:
            ev3.screen.clear()
            ev3.screen.print(myRobot.distance())
    elif state == 0:
        if ts.pressed()==True:
            state=1
            myRobot.reset()
            ev3.screen.clear()
            myRobot.drive(250)
        else:
            pass

#Line Tracking
def programm3():
    if SmallMotor.angle()== 90:
        SmallMotor.run_angle(20,-90, then=Stop.HOLD)
    myRobot.drive(40, TurnRate())

#Spezialprogramm
def programm4():
    if SmallMotor.angle()==0:
        SmallMotor.run_angle(20, 90, then=Stop.HOLD)
    else:
        if cs.color()==Color.RED:
            Quadrat()
        elif cs.color()==Color.BLUE:
            Drehung()
        elif cs.color()==Color.GREEN:
            Dreieck()
        else:
            pass

#Reset Programm
def programm0():
    myRobot.stop()
    ev3.screen.clear()
    state = 0
    Abweichung = 0
    i = 0
    x = 0
    myRobot.reset()
    if SmallMotor.angle()==90:
        SmallMotor.run_angle(20,-90, then=Stop.HOLD)

def detectProgram():
    Programm = 0
    if Button.UP in ev3.buttons.pressed():
        Programm = 1
    elif Button.RIGHT in ev3.buttons.pressed():
        Programm = 2
    elif Button.DOWN in ev3.buttons.pressed():
        Programm = 3
    elif Button.LEFT in ev3.buttons.pressed():
        Programm = 4
    elif Button.CENTER in ev3.buttons.pressed():
        Programm = 0
    else:
        pass
    return Programm

while True:
    if detectProgram() == 1:
        programm1()
    elif detectProgram() == 2:
        programm2()
    elif detectProgram() == 3:
        programm3()
    elif detectProgram() == 4:
        programm4()
    elif detectProgram() == 0:
        programm0()
    else:
        pass

    
    
