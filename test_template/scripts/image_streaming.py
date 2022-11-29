#!/usr/bin/env python3
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
cv_bridge = CvBridge()

class GetImage:
 
    def __init__(self):
        rospy.init_node('streaming_image', anonymous=True)
        sub_rgb = rospy.Subscriber("camera/rgb/image_raw",Image ,self.callback)

    def callback(self, rgb_data):
        try:
            color_image = cv_bridge.imgmsg_to_cv2(rgb_data, 'bgr8')
        except CvBridgeError as e:
            rospy.logerr(e)

        cv2.imshow("color_image", color_image)
        cv2.waitKey(1)

if __name__ == '__main__':
    try:
        gi = GetImage()
        rospy.spin()
        cv2.destroyAllWindows()
    except rospy.ROSInterruptException: 
        pass
