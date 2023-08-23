# ROS demo: creating python nodes

## Details:
* Package name: ros_demo_py_node
* Content: 2 nodes showing log levels, `rospy.on_shutdown()` and `rospy.rate(10).sleep`

## Instruction:
After create the workspace `workshop_demo_ws`:

```
cd ./src/
```

Then, create the rospackage `ros_demo_py_node` with `rospy` as dependency:

```
catkin_create_pkg ros_demo_py_node rospy
```

Then create the sample node for log levels and `rospy.on_shutdown()`:
```py
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
    
```

Then create the sample node for `rospy.rate(10)`:

```py
import rospy
import random

if __name__ == "__main__":
    rospy.init_node("ROSPY_SpinOnce_Loop_random_node")

    rate = rospy.Rate(10)
    
    counter = 0
    while not rospy.is_shutdown():
        
        # hello_str = "ROSPY: hello world %d" % counter

        i = random.randint(1000, 1000000)
        start_time = rospy.get_time()
        rospy.loginfo(f"ROSPY: starting this loop at {rospy.get_time()}")
        for j in range(i):
            j = j+1
        print(f"ROSPY: doing {j} random loops takes {rospy.get_time()-start_time}")
        rate.sleep()
        counter += 1

```

Then, adding your node into the CMakeLists.txt:

```cmake
catkin_install_python(PROGRAMS
  <python_source_code_1.py>
  <python_source_code_2.py>
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

Now, you can build and play with your ros nodes.