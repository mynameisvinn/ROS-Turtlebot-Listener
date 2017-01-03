# ROS Turtlebot Listener

## what is this?
learn ros by creating nodes, topics, and all that other good stuff.

## run

### 1) fetch listener script
```
git clone https://github.com/mynameisvinn/ROS-Turtlebot-Listener
cd catkin_ws
catkin_make # need to use cmake even for python nodes
```
for more information, try http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

### 2) run turtlebot
from terminal 1, do
```
roslaunch turtlebot_bringup minimal.launch
```
from terminal 2, do
```
roslaunch turtlebot_teleop keyboard_teleop.launch
```
for more information, visit http://www.artificialhumancompanions.com/autonomous-deep-learning-robot-the-missing-instructions/#more-10

### 3) execute listener
from terminal 3, do
```
roscore
```
you need roscore because listener does not have a launch package, and therefore needs to find ros master through roscore.

from terminal 4, do
```
cd catkin_ws
source ./devel/setup.bash
rosrun beginner_tutorials listener.py
```

