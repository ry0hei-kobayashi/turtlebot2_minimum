import rospy
import cv2
import traceback
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

cv_bridge = CvBridge()

path = "/home/roboworks/education_ws/src/test_template/data/haarcascades/haarcascade_frontalface_default.xml"


class HumanTracking:
    def __init__(self):
        sub_rgb = rospy.Subscriber("/camera/rgb/image_raw",Image,self.get_image_callback)
        self.frame = []
        self.cascade = cv2.CascadeClassifier(path)
        self.twist = Twist()

    def get_image_callback(self,msg):
        self.frame = cv_bridge.imgmsg_to_cv2(msg,"bgr8")

    def HaarCascade(self):
        frame = self.frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = self.cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y+h), (0, 0, 200), 3)
        self.face = face
        cv2.imshow("frame",frame)
        cv2.waitKey(1)

    def RobotMove(self):
        size = self.frame.shape
        if 0 < len(self.face):
            x,y,w,h = self.face[0]
            if x < size[1]/3:
                self.twist.linear.x = 0
                self.twist.angular.z = 0.8
            elif size[1]*(2/3) < x:
                self.twist.linear.x = 0
                self.twist.angular.z = -0.8
            else:
                self.twist.linear.x = 0.07
                self.twist.angular.z = 0


if __name__ == "__main__":
    try:
        rospy.init_node("human_tranking",anonymous=True)
        pub=rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=1)
        r = rospy.Rate(10)
        HT = HumanTracking()
        while not rospy.is_shutdown():
            if 0 < len(HT.frame):
                HT.HaarCascade()
                HT.RobotMove()
                pub.publish(HT.twist)

            r.sleep()
    except:
        traceback.print_exc()

