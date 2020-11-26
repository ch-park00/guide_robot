# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32
import os
import time
import subprocess
# 로봇이 목적지에 도착 시 해당 목적지의 flag 값에 해당하는 ROS Message를 받음.
# 그 때, 음성 출력 후 바로 종료

def callback(data):
   
   # 목적지가 하나인 경우.
   os.system("ffplay -nodisp -autoexit dst_record.mp3")
   os.system("rostopic pub -1 inputOrder std_msgs/Int32 0")
   os.system("echo 0 > test.txt")
   
   
def listener():
   rospy.init_node('result_flag')
   rospy.Subscriber("r_flag", Int32, callback)
   rospy.spin()

listener()
