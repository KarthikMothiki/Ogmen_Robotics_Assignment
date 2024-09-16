# bot_control

The `bot_control` package contains two main scripts:
- `move.py` - A script to control a robot to move through a series of waypoints.
- `reading_laser.py` - A script to filter and publish laser scan data.

## Package Structure

```
.
├── bot_control
│   ├── __init__.py
│   ├── move.py
│   └── reading_laser.py
├── LICENSE
├── package.xml
├── resource
│   └── bot_control
├── setup.cfg
├── setup.py
└── test
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py

3 directories, 11 files

```

## Installation and Setup

**Build the Package:**
   Navigate to your workspace and build the `bot_control` package using `colcon`:

   ```bash
   cd ~/karthik_ws
   colcon build --packages-select bot_control
   . install/setup.bash
   ```
## Scripts
**move.py**
This script moves the robot through predefined waypoints and aligns its orientation at each waypoint.
```
ros2 run bot_control move_robot
```

https://drive.google.com/file/d/1XSYWK0PRhd1JiB8qL457hNljVQPyJThK/view?usp=sharing

**reading_laser.py**
This script filters laser scan data and publishes it on a new topic /filtered_scan.

```
ros2 run bot_control laser_filter
```

![Screenshot from 2024-09-17 00-03-01](https://github.com/user-attachments/assets/b1fd823b-752b-4882-aaf6-1c9d8c5db8d9)

