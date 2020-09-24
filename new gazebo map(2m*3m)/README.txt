roslaunch turtlebot3_gazebo turtlebot3_world.launch – 가제보실행
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping – SLAM실행
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch – 터틀봇 조종
rosrun map_server map_saver -f ~/map – 지도 저장

해당 turtlebot3_world.launch파일을 launch파일 첨부한 파일명으로 바꾸어 돌리면된다.



맵파일 네비게이션 진행 ( 중앙 가로막는 벽 없음, 65cm )

roslaunch turtlebot3_gazebo map_wall65_nocenterwall.launch
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map_wall65_nocenterwall .yaml

맵파일 네비게이션 진행 ( 중앙 가로막는 벽 있음, 65cm )
– 이 경우 인코스로 도는것 때문에 버벅임
연균이형 말대로 로봇 진행방향을 벽이 어느정도 거리둘지 파라미터 조절해야 제대로 사용가능할듯

roslaunch turtlebot3_gazebo map_wall65_hascenterwall.launch
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map_wall65_hascenterwall.yaml

맵파일 네비게이션 진행 ( 중앙 가로막는 벽 없음, 75cm )
roslaunch turtlebot3_gazebo map_wall75_nocenterwall.launch
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map_wall75_nocenterwall.yaml