# bot_description

This package contains the World file  of the given environment.

## How to test the package

1. Build the package:
    ```bash
    cd ~/your_name_ws
    colcon build --packages-select bot_world
    ```

2. Source the workspace:
    ```bash
    source install/setup.bash
    ```

3. Launch the robot description (using your custom launch file if applicable):
    ```bash
    ros2 launch bot_description task.launch.py
    ```

4. This should launch the robot model in Gazebo with the specified specified environments.

file:///home/km/Pictures/Screenshots/Screenshot%20from%202024-09-16%2022-39-14.png
-81:-6:85:47
