# Turtle Movement ROS Package

This ROS package provides a simple Python script to control the movement of a turtle in the ROS environment. The turtle moves in a predefined pattern consisting of an upper circle, downward line, and a downward arc-circle.

## Prerequisites

- ROS (Robot Operating System)
- Python (tested with Python 2.7)

## Installation

1. Clone this repository to your ROS workspace:

   ```bash
   git clone https://github.com/your_username/turtle_movement_ros.git
Build the package using catkin_make:
   ```bash
   cd path_to_your_ros_workspace
   catkin_make
```
   
## Usage

1. Make sure you have ROS environment set up properly and a ROS master running.

2. Launch the turtlesim simulator (if not already running):

   ```bash
   roscore
   rosrun turtlesim turtlesim_node 
3.Run the turtle movement script:
   ```bash
   rosrun turtle_movement_ros draw_9.py
