from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('create3_pkg')
    params_file = os.path.join(pkg_share, 'config', 'slam_params.yaml')

    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[params_file],
            remappings=[
                #  Si tu LiDAR publica en otro tópico (ej: /robot1/scan), cámbialo aquí
                ('/scan', '/scan'),
            ],
        ),
    ])
