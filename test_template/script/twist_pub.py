#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from time import sleep

rospy.init_node('twist_publlisher')
pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size = 10)

while not rospy.is_shutdown():
    twist = Twist()
    twist.linear.x = 0.2
    twist.angular.z = 0.5

    print(twist)
    pub.publish(twist)
