# draw a square
have the turtlebot go around in a square. inspired by (tend.ai)[https://github.com/markwsilliman/turtlebot]

## why draw a square?
learn best practices on organizing ros code - in oop or scripts?

## how to create?
usual steps of creating package, downloading script, making...
```
cd catkin_ws/src
catkin_create_pkg ros_drawsquare std_msgs rospy
cd ros_drawsquare
mkdir script
wget https://raw.githubusercontent.com/markwsilliman/turtlebot/master/draw_a_square.py
cd ~catkin_ws
catkin_make
```

## how to run?
* terminal 1, do `roslaunch turtlebot_bringup minimal.launch`

since we didnt make the python script executable, do this
* terminal 2, go to scripts directory and do `python draw_a_square.py`

you can listen in on navi commands
* terminal 3, do `rostopic echo /cmd_vel_mux/input/navi`


