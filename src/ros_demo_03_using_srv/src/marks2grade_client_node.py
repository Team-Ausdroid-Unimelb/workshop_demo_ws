#!/usr/bin/env python
from ros_demo_srv_creator.srv import Marks2Grade
import rospy
import sys

service_name = "marks_to_grade"


def service_caller(marks):
    
    rospy.loginfo("waiting for service %s",service_name)
    rospy.wait_for_service(service_name)
    try:
        rospy.loginfo("Getting service now")
        service_runner = rospy.ServiceProxy(service_name,Marks2Grade)
        rospy.loginfo("Calling service now")
        res = service_runner(marks)
        rospy.loginfo("The marks is %f, the grade is %s"%(marks,res.grade))
    except rospy.ServiceException:
         rospy.logwarn("service calling failed")
    

if __name__ == "__main__":

    # without the init, no ros log will get printed
    rospy.init_node("marks2fgrade_client_node")
    if len(sys.argv) == 2:
        marks = float(sys.argv[1])
    else:
        rospy.logerr("need exactly one argument for marks")
        sys.exit(1)
    
    service_caller(marks)