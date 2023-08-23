#include "ros/ros.h"

/**
 * This tutorial demonstrates simple ros node in the ROS system.
 */
int main(int argc, char **argv)
{

  ros::init(argc, argv, "ROSCPP_Spin_Node", ros::init_options::NoSigintHandler);
  ros::NodeHandle n;

  std::cout << "Hello World!";
  ROS_INFO("Before spin");
  ros::spin();

  // the following line will never work
  ROS_INFO("After spin");
  return 0;
}

