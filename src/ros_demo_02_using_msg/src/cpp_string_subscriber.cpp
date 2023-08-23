#include "ros/ros.h"

#include "std_msgs/String.h"


void chattingCallback(const std_msgs::String::ConstPtr& msg)
{
    ROS_INFO("Receving: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
    ros::init(argc,argv, "roscpp_string_subscriber");
    ros::NodeHandle n;

    ros::Subscriber sub = n.subscribe("chatting",1000,chattingCallback);

    ros::spin();

    return 0;
}

