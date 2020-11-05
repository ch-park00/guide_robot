#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include <cstdlib>
#include <iostream>
#include <unistd.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::Int32>("inputOrder", 10);

  ros::Rate loop_rate(10);
  std_msgs::Int32 msg;
  msg.data=atoi(argv[1]);
  usleep(1000*200);
  chatter_pub.publish(msg);
  ros::spinOnce();
  loop_rate.sleep();
  

  return 0;
}
