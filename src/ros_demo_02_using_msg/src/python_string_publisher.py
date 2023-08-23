#!/usr/bin/env python

import rospy

from std_msgs.msg import String

def sender():
    pub = rospy.Publisher('chatting',String,queue_size=10)
    rospy.init_node("rospy_string_publisher",anonymous=False)
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        message_str = "hello world %s" % rospy.get_time()

        rospy.loginfo(message_str)
        pub.publish(message_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        sender()
    except:
        pass