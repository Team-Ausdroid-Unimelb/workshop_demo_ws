#include "ros/ros.h"
#include "ros_demo_srv_creator/Marks2Grade.h"

bool service_runner(ros_demo_srv_creator::Marks2Grade::Request &req,
                    ros_demo_srv_creator::Marks2Grade::Response &res)
                    
{
    res.grade = "N/A";
    if (req.marks >=80)
    {
        res.grade = "H1";
    }
    else if (req.marks >=75)
    {
        res.grade = "H2A";
    }
    else if (req.marks >=70)
    {
        res.grade = "H2B";
    }
    else if (req.marks >=65)
    {
        res.grade = "H3";
    }
    else if (req.marks >=50)
    {
        res.grade = "P";
    }else
    {
        res.grade = "N";
    }
    ROS_INFO("request: [marks: %f] received",req.marks);
    ROS_INFO("response: [grade: %s] sent", res.grade.c_str());
    return true;
}

int main(int argc, char ** argv)
{
    ros::init(argc,argv, "marks2grade_server_node");
    ros::NodeHandle n;
    ros::ServiceServer service = n.advertiseService("marks_to_grade",service_runner);
    ROS_INFO("Server is ready");
    ros::spin();
    return 0;
}