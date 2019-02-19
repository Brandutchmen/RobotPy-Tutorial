#!/usr/bin/python
# -*- coding: utf-8 -*-

import wpilib

class Drive(object):

    '''
    This is a simple Drive class. We can put our drive code here to make
    the code neater and work on making more complicated functions to be called
    from our robot.py
    '''

    def __init__(self, robotDrive):
        self.robotDrive = robotDrive

    def masterDrive(self, posX, posY):
        self.robotDrive.arcadeDrive(posX, posY)
