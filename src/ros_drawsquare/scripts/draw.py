#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import radians

def DrawASquare():
    # initiliaze a ros node called drawawquare
    rospy.init_node('drawasquare', anonymous=False)

    # What to do you ctrl + c    
    rospy.on_shutdown(myshutdowncallback)
        
    # create a publisher called "cmd vel"
    cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
     
	# 5 HZ - that means each iteration in a range loop takes 0.2 sec
    r = rospy.Rate(5);

	# create two different Twist() variables.  One for moving forward.  One for turning 45 degrees.

    # let's go forward at 0.2 m/s
    move_cmd = Twist()
    move_cmd.linear.x = 0.2
	

    #let's turn at 45 deg/s
    turn_cmd = Twist()
    turn_cmd.linear.x = 0
    turn_cmd.angular.z = radians(45); #45 deg/s in radians/s

	#two keep drawing squares.  Go forward for 2 seconds (10 x 5 HZ) then turn for 2 second
    while not rospy.is_shutdown():
        # go forward 0.4 m (2 seconds * 0.2 m / seconds)
        rospy.loginfo("Going Straight")
        for x in range(0,10): # since it's at 5hz, 10 iterations moves it for 2 seconds
            cmd_vel.publish(move_cmd) # for each iter, post command
            r.sleep()
        # turn 90 degrees
        rospy.loginfo("Turning")
        for x in range(0,10):
            cmd_vel.publish(turn_cmd)
            r.sleep()            
        
def myshutdowncallback():
    rospy.loginfo("Stop Drawing Squares")
    cmd_vel.publish(Twist())
    rospy.sleep(1)
 
if __name__ == '__main__':
    DrawASquare()