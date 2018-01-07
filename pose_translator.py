#!/usr/bin/python

PKG = 'pose_translator'
import roslib; roslib.load_manifest(PKG)
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped

pub = rospy.Publisher('/pose', PoseWithCovarianceStamped, queue_size=200)


def callback(data):
    header = data.header
    pose_w_c = data.pose
    msg = PoseWithCovarianceStamped()
    msg.header = header
    msg.pose = pose_w_c
    pub.publish(msg)
    
    
def listener():
    rospy.init_node('pose_translator')
    rospy.Subscriber("/imu_odom", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
