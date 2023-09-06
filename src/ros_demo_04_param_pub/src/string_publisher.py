#!/usr/bin/env python
import rospy
from std_msgs.msg import String

param_str = "test_param"


def talker():
    pub = rospy.Publisher('testing_topic', String, queue_size=10)
    rospy.init_node('rospy_string_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        test_param = rospy.get_param(param_name=param_str,default=-3)
        # test_param = -3
        # if rospy.has_param(param_str):
        #     test_param = rospy.get_param(param_str)
        hello_str = "%d hello world %s" % (test_param,rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass