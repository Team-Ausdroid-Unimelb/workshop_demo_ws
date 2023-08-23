#include "ros/ros.h"

/**
 * This tutorial demonstrates simple ros node in the ROS system.
 */
int main(int argc, char **argv)
{

  ros::init(argc, argv, "ROSCPP_SpinOnce_Node", ros::init_options::NoSigintHandler);

  ros::NodeHandle n;

  std::cout << "Hello World!";
  ROS_INFO("Before spinOnce");
  ros::spinOnce();
  ROS_INFO("After spinOnce");
  return 0;
}

