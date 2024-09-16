# bot_description

This package contains the URDF description of the robot.

## How to test the package

1. Build the package:
    ```bash
    cd ~/your_name_ws
    colcon build --packages-select bot_description
    ```

2. Source the workspace:
    ```bash
    source install/setup.bash
    ```

3. Launch the robot description:
    ```bash
    ros2 launch bot_description spawn.launch.py
    ```

4. This should launch the robot model in RViz or other specified environments.
   ```bash
    ros2 launch bot_description rviz_launch.py
    ```
5. For the teleop node:
   ```
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```

### Troubleshooting
- Make sure the URDF path is correct in the launch file.
- Ensure dependencies like `xacro` and `robot_state_publisher` are installed.
