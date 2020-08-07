SLAM 스터디 관련

맵파일(mart) launch
- roslaunch turtlebot3_gazebo mart.launch

gmapping 실행
- roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

원격조작
- roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

SLAM으로 만든 맵 import
- rosrun map_server map_saver -f ~/map

Navigation
- roslaunch turtlebot3_navigation turtlebot3_navigation.launch