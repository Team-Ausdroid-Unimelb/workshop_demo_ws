#include "ros/ros.h"
/**
 * This tutorial demonstrates simple ros node in the ROS system.
 */
int main(int argc, char **argv)
{

  ros::init(argc, argv, "ROSCPP_Loop_SpinOnce_Node", ros::init_options::NoSigintHandler);

  ros::NodeHandle n;

  // the frequency your node spin with ROS within 1 second
  ros::Rate loop_rate(30);
  std::cout << "Hello World!";

  int count = 0;
  while (ros::ok())
  {
    ROS_INFO("ROSCPP: %d", count);
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }

  return 0;
}

