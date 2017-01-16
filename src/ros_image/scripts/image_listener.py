#! /usr/bin/python

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

'''
reference: http://answers.ros.org/question/210294/ros-python-save-snapshot-from-camera/
'''

import rospy
from sensor_msgs.msg import Image # ROS Image message
from cv_bridge import CvBridge, CvBridgeError # ROS Image message -> OpenCV2 image converter
import cv2

bridge = CvBridge() # Instantiate CvBridge

def image_callback(msg):
    '''
    callback func is applied when a new message is posted on topic
    '''
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite('camera_image.jpeg', cv2_img)

def main():
    rospy.init_node('image_listener') # create a new node called image_listener
    topic = "/camera/rgb/image_raw" # what topic to subscribe to?
    
    # subscribe applies callback when a new Image is posted to topic
    # remember ros topics are strongly typed
    rospy.Subscriber(topic, Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    main()