import os
from launch import LaunchDescription
from launch.actions import LogInfo, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Define URIs to your launch files and configurations
    map_file = LaunchConfiguration('map_file', default='./my_map_save.yaml')

    # Launch file for online async
    online_async_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('my_bot'), 'launch', 'online_async_launch.py'
        )])
    )

    # Launch file for localization
    localization_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('nav2_bringup'), 'launch', 'localization_launch.py'
        )]),
        launch_arguments={'map': map_file, 'use_sim_time': 'true'}.items()
    )

    # Launch file for navigation
    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('nav2_bringup'), 'launch', 'navigation_launch.py'
        )]),
        launch_arguments={'use_sim_time': 'true', 'map_subscribe_transient_locale': 'true'}.items()
    )

    return LaunchDescription([
        LogInfo(msg='Starting online async launch file...'),
        online_async_launch,
        LogInfo(msg='Starting localization launch file...'),
        localization_launch,
        LogInfo(msg='Starting navigation launch file...'),
        navigation_launch
    ])
