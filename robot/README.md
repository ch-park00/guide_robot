### 로봇 관련

### TurtleBot 강의

* ROS Courses: https://www.youtube.com/playlist?list=PLRG6WP3c31_VIFtFAxSke2NG_DumVZPgw

* 강의자료 pdf: https://github.com/robotpilot/ros-seminar

* 참고서적, ROS 로봇 프로그래밍: https://book.naver.com/bookdb/book_detail.nhn?bid=12443870

* emanual 사이트: http://emanual.robotis.com/docs/en/platform/turtlebot3/overview/



### 샘플코드

* ROS 튜토리얼: https://github.com/ROBOTIS-GIT/ros_tutorials

* 터틀봇3 튜토리얼: https://github.com/ROBOTIS-GIT/turtlebot3

### 튜토리얼 샘플 코드 다운로드 후 빌드

cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/ros_tutorials.git
cd ~/catkin_ws
catkin_make

### 원하는 패키지만 make하기를 원하는 경우에는 다음의 명령어를 사용한다.
### catkin_make -DCATKIN_WHITELIST_PACKAGES="000"

### turtlebot3 튜토리얼 샘플 코드에서 SLAM 및 Navigation Test를 위해 필요한 패키지 설치 
### http://turtlebot3.robotis.com 공식 위키 사이트 참조

sudo apt install ros-kinetic-joy ros-kinetic-teleop-twist-joy ros-kinetic-teleop-twist-keyboard ros-kinetic-laser-proc ros-kinetic-rgbd-launch ros-kinetic-depthimage-to-laserscan ros-kinetic-rosserial-arduino ros-kinetic-rosserial-python ros-kinetic-rosserial-server ros-kinetic-rosserial-client ros-kinetic-rosserial-msgs ros-kinetic-amcl ros-kinetic-map-server ros-kinetic-move-base ros-kinetic-urdf ros-kinetic-xacro ros-kinetic-compressed-image-transport ros-kinetic-rqt-image-view ros-kinetic-gmapping ros-kinetic-navigation

### 이 실습을 위한 코드 다운로드 후 빌드

cd ~/catkin_ws/src/
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws && catkin_make
