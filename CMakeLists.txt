cmake_minimum_required(VERSION 2.8.3)
project(keyboard_control)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)



# generate_messages(
#   DEPENDENCIES
#   std_msgs
# )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES keyboard_control
#  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


#catkin_install_python(PROGRAMS
#   teleop_twist_keyboard.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)
