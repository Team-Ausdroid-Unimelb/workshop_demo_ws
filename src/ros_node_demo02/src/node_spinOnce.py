import rospy

if __name__ == "__main__":
    rospy.init_node("ROSPY_SpinOnce_node")

    print("this is print")
    rospy.loginfo("this is log info")
    rospy.logdebug("this is debug")
    rospy.logwarn("this is warn")
    rospy.logerr("this is error")
