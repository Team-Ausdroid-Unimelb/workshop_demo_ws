#!/usr/bin/env python
import rospy

def shutdown():
    # this message will appear when shutdown
    rospy.logerr("Output before shutdown")
    rospy.sleep(1)

if __name__ == "__main__":
    rospy.init_node("ROSPY_SpinOnce_Loop_node")

    print("this is print")
    rospy.loginfo("this is log info")
    rospy.logdebug("this is debug")
    rospy.logwarn("this is warn")
    rospy.logerr("this is error")
    rospy.on_shutdown(shutdown)
    rospy.spin()
    
