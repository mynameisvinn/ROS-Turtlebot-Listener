#!/usr/bin/env python

'''
original script from http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

original listener subscribed to "chatter" topic, which was published by a talker script. messages were of "string" type.

refernece: http://answers.ros.org/question/223785/creating-a-subscriber-in-python/
'''

import rospy
# from std_msgs.msg import String # 
from geometry_msgs.msg import Twist

def callback(data):
    # changed data.data to data.linear.x - this is twist's data type
    # twist's attribute is linear.x
    # http://answers.ros.org/question/223785/creating-a-subscriber-in-python/
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.linear.x)

def listener():
    rospy.init_node('listener', anonymous=True)

    # we've modificed topic and msg type, from 'chatter' & 'string' to 'cmd_vel_mux/input/teleop' and 'Twist'
    rospy.Subscriber('cmd_vel_mux/input/teleop', Twist, callback) 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
