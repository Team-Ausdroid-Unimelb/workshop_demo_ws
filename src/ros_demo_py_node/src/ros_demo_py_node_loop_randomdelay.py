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
