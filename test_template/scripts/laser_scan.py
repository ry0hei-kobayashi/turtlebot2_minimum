#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import math 

class Laser():
    def __init__(self):
        rospy.init_node('lidar', anonymous=True)
        laser_sub = rospy.Subscriber('/scan', LaserScan , self.laser_callback)

    def laser_callback(self, laser):
    
        self.ranges = laser.ranges 
        self.angle_min = laser.angle_min
        self.angle_max = laser.angle_max
        self.angle_increment = laser.angle_increment
        self.range_min = laser.range_min
        self.range_max = laser.range_max

        while not rospy.is_shutdown():
            rospy.loginfo("Number of Rays=%d", len(self.ranges))
            rospy.loginfo("Angle [rad] min=%f max=%f", self.angle_min, self.angle_max)
            rospy.loginfo("Angle [deg] increment=%.3f", math.degrees(self.angle_increment))
            rospy.loginfo("Range [m] min=%.3f max=%.3f", self.range_min, self.range_max)
            rospy.loginfo("  0[deg]=%.3f[m]  90[deg]=%.3f[m]  180[deg]=%.3f[m]", self.ranges[0],self.ranges[90],self.ranges[180])


if __name__ == '__main__':
    try:
        ls = Laser()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

