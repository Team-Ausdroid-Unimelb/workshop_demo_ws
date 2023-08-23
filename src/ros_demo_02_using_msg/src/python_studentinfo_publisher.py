#!/usr/bin/env python

import rospy

# from std_msgs.msg import String

from ros_demo_02_using_msg.msg import StudentInfo



def sender():
    pub = rospy.Publisher('student_info_topic',StudentInfo,queue_size=10)
    rospy.init_node("rospy_studentinfo_publisher",anonymous=False)
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        message_str = "hello world %s" % rospy.get_time()
        student_info_msg = StudentInfo()
        student_info_msg.first_name = "guang"
        student_info_msg.last_name =  message_str

        rospy.loginfo(student_info_msg)
        pub.publish(student_info_msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        sender()
    except:
        pass