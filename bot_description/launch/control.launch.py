import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Teleop twist keyboard node for keyboard control
    teleop_twist_keyboard = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard',
        output='screen',
        parameters=[{'use_sim_time': 'true'}],

    )

    # Launch them all!
    return LaunchDescription([
        teleop_twist_keyboard,
    ])
