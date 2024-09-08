import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_name = 'my_bot'  # Change to your package name if different

    # Define URIs to your launch files and configurations
    world_file = LaunchConfiguration('world_file', default='./src/my_bot/worlds/house1.world')
    rviz_config = LaunchConfiguration('rviz_config', default='src/my_bot/config/house1.rviz')

    # Launch file for simulation
    launch_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'launch_sim.launch.py'
        )]),
        launch_arguments={'world': world_file}.items()
    )

    # Node for RViz2 configuration
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config],
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    return LaunchDescription([
        LogInfo(msg='Starting Gazebo simulation...'),
        launch_sim,
        LogInfo(msg='Starting RViz2...'),
        rviz_node
    ])
