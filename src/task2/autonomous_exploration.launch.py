import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    turtlebot3_gazebo = get_package_share_directory('turtlebot3_gazebo')
    slam_toolbox = get_package_share_directory('slam_toolbox')
    nav2_bringup = get_package_share_directory('nav2_bringup')

    # Launch Gazebo with turtlebot3_world
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(turtlebot3_gazebo, 'launch', 'turtlebot3_world.launch.py')
        )
    )

    # Launch SLAM Toolbox (online async mode)
    slam_launch = TimerAction(
        period=5.0,
        actions=[IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(slam_toolbox, 'launch', 'online_async_launch.py')
            ),
            launch_arguments={'use_sim_time': 'true'}.items()
        )]
    )

    # Launch Nav2
    nav2_launch = TimerAction(
        period=10.0,
        actions=[IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_bringup, 'launch', 'navigation_launch.py')
            ),
            launch_arguments={'use_sim_time': 'true'}.items()
        )]
    )

    # Launch Explore Lite
    explore_node = TimerAction(
        period=15.0,
        actions=[Node(
            package='explore_lite',
            executable='explore',
            name='explore',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'robot_base_frame': 'base_footprint',
                'costmap_topic': 'map',
                'costmap_updates_topic': 'map_updates',
                'visualize': True,
                'planner_frequency': 0.33,
                'progress_timeout': 30.0,
                'potential_scale': 3.0,
                'gain_scale': 1.0,
                'transform_tolerance': 0.3,
                'min_frontier_size': 0.75,
            }]
        )]
    )

    return LaunchDescription([
        gazebo_launch,
        slam_launch,
        nav2_launch,
        explore_node,
    ])
