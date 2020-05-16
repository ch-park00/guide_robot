#  ROS 설치 테스트 코드. 
# 각 명령어는 하나의 터미널에서 하나씩 수행해야 함
roscore

rosrun turtlesim turtlesim_node

rosrun turtlesim turtle_teleop_key

rosrun rqt_graph rqt_graph
