#!/usr/bin/env python3 # <---- This runs the code

'''
Part 2: Simple Classes
'''

import wpilib
from wpilib import drive
from components import drive #This tells our robot.py file to import the drive.py file

class MyRobot(wpilib.IterativeRobot): #<-- This is the base class for the entire robot

    def robotInit(self):

        #Motors
        self.leftMotor = wpilib.Talon(0)
        self.rightMotor = wpilib.Talon(1)

        #User Input
        self.playerOne = wpilib.XboxController(0)# <-- This is for using Xbox controllers

        #Setup robotDrive
        self.robotDrive = wpilib.drive.DifferentialDrive(self.leftMotor, self.rightMotor)

        #Initialize drive.py
        self.drive = drive.Drive(self.robotDrive)

    def teleopPeriodic(self):

        #Drive
        self.drive.masterDrive(self.playerOne.getY(0), self.playerOne.getX(0))

if __name__ == "__main__": #This is the end of the code. Don't mess with this part =)
    wpilib.run(MyRobot)
