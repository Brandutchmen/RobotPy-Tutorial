#!/usr/bin/env python3 # <---- This runs the code

'''
Start by importing your libraries. Refer to http://robotpy.readthedocs.io/projects/wpilib/en/latest/api.html
for the libraries and their API handles.

Wpilib - Base FRC package
'''

import wpilib

class MyRobot(wpilib.IterativeRobot): #<-- This is the base class for the entire robot

    '''
    Now we are going to call our functions. These functions are called by the Field Management system
    when the match starts. General rule of thumb:

        Any function that ends with "INIT" is an initialization function. It is only called once. You should NOT
        have your robot move during this time. These are good for calling functions, reseting encoders, etc.

        Any fuction that ends with "Periodic" is a loop. These are were you put your controls into so you an move
        and do.
    '''

    def robotInit(self):
        '''
        This is the FIRST Thing that gets called for your robot. Remember that python works from top to bottom.
        So you will need to define everything before you implement it.
        '''

        self.leftMotor = wpilib.Talon(0) # <-- This is what links our PWM port on the CRIO to a physical ESC.
        self.rightMotor = wpilib.Talon(1)

        #User Input
        self.playerOne = wpilib.XboxController(0)# <-- This is for using Xbox controllers


        #Now we need to link our motors to the RobotDrive class

        self.robotDrive = wpilib.RobotDrive(self.leftMotor, self.rightMotor)


    def disabledInit(self):
        '''
        This is called when the robot is disabled. You will very rarely have to use this one.
        '''
        pass

    def autonomousInit(self):
        '''
        This is executed 1 time right before the autonomousPeriodic runs.
        This is good for setting up autonomous only variables.
        '''
        pass

    def autonomousPeriodic(self):
        '''
        We will go over Autonomous modes in a future part. For now leave this as just pass
        '''
        pass

    def teleopInit(self):
        '''
        This is called once right before teleopPeriodic is called.
        You can use this to effectively change things after autonomous.
        '''
        pass

    def teleopPeriodic(self):

        '''
        Now we can call the robotDrive class. We are going to set this one up for arcadeDrive.

        self.robotDrive.arcadeDrive(Forward/Backwards Axis, Rotation axis)
        '''

        #Drive
        self.robotDrive.arcadeDrive(self.playerOne.getY(0), self.playerOne.getX(0))

if __name__ == "__main__": #This is the end of the code. Don't mess with this part =)
    wpilib.run(MyRobot)
