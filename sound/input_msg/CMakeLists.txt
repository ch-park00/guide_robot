cmake_minimum_required(VERSION 2.8.3)
project(input_msg)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

catkin_package(
  LIBRARIES input_msg
  CATKIN_DEPENDS roscpp std_msgs
)
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(input_talker src/input_talker.cpp)
add_dependencies(input_talker ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(input_talker ${catkin_LIBRARIES})


