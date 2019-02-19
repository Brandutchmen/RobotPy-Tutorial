# Part 1: The Basics

Congratulations! You are looking to code your robot using Robotpy.


Robotpy runs a "robot.py" file on the robot. You create this file in it's own directory.

### For Mac Users:

`python3 robotpy sim`

### For PC Users:

`py -3 robotpy sim`


This command runs your robot.py file in the simulator that comes with pyfrc.

After you have tested your code and are ready to deploy it to your robot, use this command to deploy the code to your robot.

### For Mac Users:

`python3 robot.py deploy`

### For Pc Users:

`py -3 robot.py deploy`

WARNING! Deploying your code transfers the *** ENTIRE *** directory that robot.py is in to the robot. Always put your robot.py into a folder with robot-only code. This will make your deploys a lot faster and could save issues with storage on the RoboRio.
