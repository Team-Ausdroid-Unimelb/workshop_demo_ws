#include "ros/ros.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "ROSCPP_Spin_Node", ros::init_options::NoSigintHandler);

    ros::NodeHandle n;

    std::cout << "Hello World!";
    ROS_INFO("Before spin");
    ros::spin();

    ROS_INFO("After spin");
    return 0;
}