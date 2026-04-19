# Task 2: Autonomous Exploration with TurtleBot3

## Overview
This package performs autonomous exploration using TurtleBot3 in a Gazebo simulation.
The robot automatically maps an unknown environment using SLAM Toolbox, Nav2, and Explore Lite.

## Dependencies
- ROS 2 Jazzy
- slam_toolbox
- nav2_bringup
- turtlebot3_gazebo
- explore_lite (m-explore-ros2)

## Installation
```bash
sudo apt install -y ros-jazzy-slam-toolbox ros-jazzy-navigation2 ros-jazzy-nav2-bringup ros-jazzy-turtlebot3*
cd ~/kanika/src && git clone -b ros2 https://github.com/robo-friends/m-explore-ros2.git
cd ~/kanika && colcon build --symlink-install
source ~/kanika/install/setup.bash
```

## Launch Instructions

### Terminal 1 - Gazebo
```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### Terminal 2 - SLAM
```bash
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=true
```

### Terminal 3 - Nav2
```bash
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true
```

### Terminal 4 - Explore Lite
```bash
ros2 run explore_lite explore --ros-args -p use_sim_time:=true -p robot_base_frame:=base_footprint -p visualize:=true
```

### Terminal 5 - RViz
```bash
ros2 launch nav2_bringup rviz_launch.py
```

## Save Map
```bash
ros2 run nav2_map_server map_saver_cli -f ~/kanika/src/task2/explored_map
```
