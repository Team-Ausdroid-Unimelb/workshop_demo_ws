#include "ros/ros.h"

#include "std_msgs/String.h"
#include "ros_demo_02_using_msg/StudentInfo.h"


void chattingCallback(const ros_demo_02_using_msg::StudentInfo::ConstPtr& msg)
{
    ROS_INFO("Receving: [%s]", msg->last_name.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc,argv, "roscpp_studentinfo_subscriber");
    ros::NodeHandle n;

    ros::Subscriber sub = n.subscribe("student_info_topic",1000,chattingCallback);

    ros::spin();

    return 0;
}

