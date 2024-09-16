# Ogment_Robotics_Assignment

## Overview

This repository contains a set of ROS 2 packages for controlling and describing a robot. It includes:

- **`bot_control`**: Contains Python scripts for controlling the robot, such as waypoint navigation and laser reading.
- **`bot_description`**: Contains URDF and XACRO files for describing the robot's model, including sensors and visualization configurations.
- **`bot_world`**: Contains world files for simulation and related launch configurations.

## Directory Tree
```
.
├── bot_control
│   ├── bot_control
│   │   ├── __init__.py
│   │   ├── move.py
│   │   └── reading_laser.py
│   ├── LICENSE
│   ├── package.xml
│   ├── resource
│   │   └── bot_control
│   ├── setup.cfg
│   ├── setup.py
│   └── test
│       ├── test_copyright.py
│       ├── test_flake8.py
│       └── test_pep257.py
├── bot_description
│   ├── CMakeLists.txt
│   ├── include
│   │   └── bot_description
│   ├── launch
│   │   ├── bot.launch.py
│   │   ├── control.launch.py
│   │   ├── rviz_launch.py
│   │   └── spawn.launch.py
│   ├── LICENSE
│   ├── package.xml
│   ├── rviz
│   │   └── bot_rviz.rviz
│   ├── src
│   ├── urdf
│   │   ├── camera.xacro
│   │   ├── gazebo_control.xacro
│   │   ├── inertial_macros.xacro
│   │   ├── lidar.xacro
│   │   ├── robot_core.xacro
│   │   └── robot.urdf.xacro
│   └── worlds
│       ├── empty_world.world
│       └── new_world.world
├── bot_world
│   ├── CMakeLists.txt
│   ├── include
│   │   └── bot_world
│   ├── launch
│   │   └── task.launch.py
│   ├── LICENSE
│   ├── package.xml
│   ├── src
│   └── worlds
│       └── new_world.world
└── LICENSE

18 directories, 33 files

```
## Utilization
Create your workspace
```
  source /opt/ros/humble/setup.bash
  source /usr/share/gazebo/setup.bash
  
  mkdir -p ~/karthik_ws/src
  cd karthik_ws
  colcon build
  source install/setup/bash
```
Clone the repo into your src/ folder of the workspace
```
cd <path_to_your ws/src>
git clone https://github.com/KarthikMothiki/Ogmen_Robotics_Assignment/
```
Now build the packages
```
cd ..
colcon build
source install/setup.bash
```

