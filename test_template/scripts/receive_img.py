#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

def GetImage():
    rospy.init_node('receive_image', anonymous=True)
    sub = rospy.Subscriber('image_data', Image, Callback) 
    
def Callback(rgb_image):
    bridge = CvBridge()
    try:
        img = bridge.imgmsg_to_cv2(rgb_image, 'bgr8')
    except CvBridgeError as e:
        rospy.logerr(e)

    #print(img)
    cv2.imshow("rgb", img)
    cv2.waitKey(1)
    
if __name__ == '__main__':
    try:
        GetImage()
        rospy.spin()
        cv2.destroyAllWindows()
    except rospy.ROSInterruptException:
        pass
