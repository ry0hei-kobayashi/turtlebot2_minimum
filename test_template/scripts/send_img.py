#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

def LoadImage():
    rospy.init_node('load_image', anonymous=True)

    pub = rospy.Publisher('image_data', Image, queue_size=10)
    img = cv2.imread('/home/roboworks/education_ws/src/test_template/data/baboon.jpg')

    bridge = CvBridge()
    img = bridge.cv2_to_imgmsg(img, encoding="bgr8")

    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        pub.publish(img)
        rate.sleep()

if __name__ == '__main__':
    try:
        LoadImage() 
    except rospy.ROSInterruptException:
        pass

