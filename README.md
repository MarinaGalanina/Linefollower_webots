# Linefollower with python controller in webots

![linefollower](https://user-images.githubusercontent.com/100734139/223786946-168082c3-6dc1-42a8-b4c4-ded2ce0b2cc9.jpg)

A line follower robot is a robot which follows a certain path controlled by a feed back mechanism. Line follower robot is consist of a base at the two ends of which the wheels are mounted. A rectangular form is used as the base.  Rigid body like a cylinder is added along with other shaped bodies inter connected with each other by joints, and each with its defined motion in particular direction.  
The line fallowing robot is one of the self-operating robots. That detects and fallows a line drawn on the area. The line is indicated by white line on a block surface or block line on a white surface. This system must be sense by the line. This application is depends upon the sensors. Here I am  using two sensors for path detection purpose. That is proximity sensor and IR sensor. The proximity sensor used for path detection and IR sensor used for obstacle detection. These sensors mounted at front end of the robot. The microcontroller is an intelligent device the whole circuit is controlled by the microcontroller.

## Controller 
Code for conroller is created in Python. Name of controller: follower.py. 
* MAX_SPEED is maximum speed of robot and can be changed. 
* TIME_STEP can be changed as well

All movements of linefollower are printed as a text:
+ "Lewo" - "Left"
+ "Prawo" - "Right"
+ " Prosto" - "Forward"
## Lines
There are two types of lines in worlds folder. User can add lines by himself in .png format.
* Basic trace without obstacles (line1.png):

![line1](https://user-images.githubusercontent.com/100734139/223786240-44179012-b126-4bf7-8dce-5904fb07b928.png)

* Trace with obstacles (line2.png):

![line2](https://user-images.githubusercontent.com/100734139/223786372-4fa89fc3-c925-4f1b-81cb-944b283cdb5d.png)
