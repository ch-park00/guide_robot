SLAM 스터디 관련

맵파일(mart) launch
- roslaunch turtlebot3_gazebo mart_new.launch

gmapping 실행
- roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

원격조작
- roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

SLAM으로 만든 맵 import
- rosrun map_server map_saver -f ~/map

Navigation
- roslaunch turtlebot3_navigation turtlebot3_navigation.launch

move_base_simple/goal 토픽 bash
- rostopic pub /move_base_simple/goal geometry_msgs/PoseStamped '{header: {stamp: now, frame_id: "map"}, pose: {position: {x: 0.7, y: 0.7, z: 0.0}, orientation: {w: 1.0}}}'
- 
move_base/cancel 토픽 bash
- rostopic pub -1 /move_base/cancel actionlib_msgs/GoalID -- {}