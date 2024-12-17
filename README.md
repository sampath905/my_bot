## 2 wheeled robot :

Features:
- Navigation
- Ball Tracking

# Navigation:
 Following are the cmds:
- ros2 launch my_bot gazebo_rviz_launch.py
- ros2 launch my_bot slam_nav_launch.py
- ros2 launch my_bot online_async_launch.py
- 
Note:Changes in Rviz to perform Navigation
  - set Global options fixed frame to map after running online_async_launch.py
  - add camera change topic to camera/imageraw
  - add laserscan change topic to scan(for thicker rays change size to 0.09)
  - add TF
  - add RobotModel change discription topic to robot description
  - add 2 maps change their topics and color scheme accordingly
  - from top left panels/add newpanel/add navigation 2(to perform waypoint navigation)
  - 
To run manually for Mapping :
- ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped

# Ball Tracking -
- ros2 launch fire_bot launch_sim.launch.py world:=./src/my_bot/worlds/house1.world
- ros2 run ball_tracker detect_ball_3d
- ros2 launch my_bot ball_tracker.launch.py sim_mode:=true

Note: rviz2 - add image,marker,change the image topic to image_out and marker topic to ball_3d_marker
