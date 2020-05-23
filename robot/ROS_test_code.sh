#  ROS 설치 테스트 코드. 
# 각 명령어는 하나의 터미널에서 하나씩 수행해야 함
roscore

rosrun turtlesim turtlesim_node

rosrun turtlesim turtle_teleop_key

rosrun rqt_graph rqt_graph


# 카메라 사용을 위해, 다음의 패키지 설치
sudo apt-get install ros-kinetic-uvc-camera

# 이 코드는 카메라를 이용한 실습. 카메라는 /dev/video0 에 등록되어 있음 
rosrun uvc_camera uvc_camera_node _device:=/dev/video0

# rqt의 경우, 에러가 발생해 rqt 실행 후 플러그인 선택하는 식으로 진행
rqt

# 센서에서 나오는 데이터 확인.
rostopic echo /image_raw
rostopic echo /turtle1/pose

