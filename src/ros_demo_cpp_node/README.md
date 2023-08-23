# ROS demo: creating cpp nodes

## Details:
* Package name: ros_demo_cpp_node
* Content: three ros node showing the `ros::spin()` and `ros::spinOnce()`

## Instruction:
After create the workspace `workshop_demo_ws`:

```
cd ./src/
```

Then, create the rospackage `ros_demo_cpp_node` with `roscpp` and `std_msgs` as dependency:

```
catkin_create_pkg ros_demo_cpp_node roscpp std_msgs
```

Then create the sample node for `ros::spin()`:
```cpp
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
```

Then create the sample node for `ros::spinOnce()`:

```cpp
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
```

Then, adding your node into the CMakeLists.txt:

```cmake
add_executable(<your_node_name> <your_node_source_code.cpp>)
target_link_libraries(<your_node_name> ${catkin_LIBRARIES})
```

Now, you can build and play with your ros nodes.