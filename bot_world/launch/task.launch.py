from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Path to the world file
    world_file = os.path.join(get_package_share_directory('bot_world'), 'worlds', 'new_world.world')

    # Gazebo launch file to load the world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': world_file}.items(),
    )

    # Path to the URDF file from bot_description package
    robot_description_path = os.path.join(get_package_share_directory('bot_description'), 'urdf', 'robot.urdf.xacro')

    # Node to spawn the robot in the center
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-file', robot_description_path, '-entity', 'your_robot', '-x', '0', '-y', '0', '-z', '1'],
        output='screen'
    )

    return LaunchDescription([gazebo, spawn_robot])