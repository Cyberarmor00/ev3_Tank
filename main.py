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
Programm = 0
state = 0
threshold = 47
PWert = 1.2
Abweichung = 0
myRobot = DriveBase(Motor(Port.A), Motor(Port.B), 45, 200)


def TurnRate():
    Abweichung = cs.reflection()-threshold
    turn = Abweichung * PWert
    return turn

#Quadrat, RED
def Quadrat():
    myRobot.turn(90)
    for i in range (2):
        myRobot.straight(400)
        myRobot.turn(90)
    myRobot.straight(400)
    i = 0

#360° Drehung, BLUE
def Drehung():
    myRobot.straight(-50)
    myRobot.turn(360)
    myRobot.straight(50)

#Dreieck, GREEN
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
    myRobot.drive(250,0)
    if distanz <= 200:
        myRobot.stop()
        myRobot.turn(120)

#Distanz Messung
def programm2():
    global state
    if state == 1:
        if ts.pressed()==True:
            state=0
            myRobot.stop()
            ev3.screen.clear()
            ev3.screen.draw_text(10,50, myRobot.distance())
        else:
            ev3.screen.clear()
            ev3.screen.draw_text(10,50, myRobot.distance())
    elif state == 0:
        if ts.pressed()==True:
            state=1
            myRobot.reset()
            ev3.screen.clear()
            myRobot.drive(250,0)
        else:
            pass
    wait(200)

#Line Tracking
def programm3():
    if SmallMotor.angle() < 90:
        SmallMotor.run_target(20,90, then=Stop.HOLD)
    myRobot.drive(40, TurnRate())

#Spezialprogramm
def programm4():
    if SmallMotor.angle()>0:
        SmallMotor.run_target(20, 0, then=Stop.HOLD)
    else:
        if cs.color()==Color.RED:
            Quadrat()
        elif cs.color()==Color.BLUE:
            Drehung()
        elif cs.color()==Color.GREEN:
            Dreieck()
        else:
            pass

#Reset Programm, reset all parameters
def programm0():
    myRobot.stop()
    myRobot.reset()
    state = 0
    Abweichung = 0
    i = 0
    x = 0
    if SmallMotor.angle()>0:
        SmallMotor.run_target(20,0, then=Stop.HOLD)

#Function to detect the programm type
def detectProgram():
    global Programm
    if Button.UP in ev3.buttons.pressed():
        ev3.speaker.say("distance control")
        Programm = 1
    elif Button.RIGHT in ev3.buttons.pressed():
        ev3.speaker.say("Distance Meassuring")
        Programm = 2
    elif Button.DOWN in ev3.buttons.pressed():
        ev3.speaker.say("Line tracking")
        Programm = 3
    elif Button.LEFT in ev3.buttons.pressed():
        ev3.speaker.say("Show me a Color")
        Programm = 4
    elif Button.CENTER in ev3.buttons.pressed():
        Programm = 0
    else:
        pass
    return Programm

#Main programm
while True:
    currentProgramm = detectProgram()
    if currentProgramm == 1:
        ev3.screen.clear()
        ev3.screen.draw_text(10, 40, currentProgramm)
        programm1()
    elif currentProgramm == 2:
        ev3.screen.clear()
        ev3.screen.draw_text(10, 40, currentProgramm)
        programm2()
    elif currentProgramm == 3:
        ev3.screen.clear()
        ev3.screen.draw_text(10, 40, currentProgramm)
        programm3()
    elif currentProgramm == 4:
        ev3.screen.clear()
        ev3.screen.draw_text(10, 40, currentProgramm)
        programm4()
    elif currentProgramm == 0:
        ev3.screen.clear()
        ev3.screen.draw_text(10, 40, "Press a button!")
        programm0()
    else:
        pass
    wait(100)

    
    
