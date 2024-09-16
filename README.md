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

Check the following README.md Files for the execution of the following questions:
Question 1 :
- [ ]  Build a new catkin workspace named **[your_name]_ws**. Then make a new package in [your_name]_ws/src named **bot_description.**
  ```
  source /opt/ros/humble/setup.bash
  source /usr/share/gazebo/setup.bash
  
  mkdir -p ~/karthik_ws/src
  cd karthik_ws
  colcon build
  source install/setup/bash
  ```
- [ ]  In the **bot_description** package, build a URDF of the given robot’s mechanical engineering drawing.
  ```
  cd src/
  ros2 pkg create --build_type ament_camake --license Apache-2.0 bot_description
  cd ..
  colcon build
  source install/setup.bash
  ```

  Check the urdf directory for the xacro files
  
- [ ]  Make a new folder bot_description/launch. It should contain the launch file (rviz.launch) to visualise the robot in rviz.
   ```
   
   ```
