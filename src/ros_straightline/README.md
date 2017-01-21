# ros straightline

## what is this?

modify keyboard teleop script. 

## why modify teleop?

learn how to hijack motor controls but posting commands to 'cmd_vel_mux/input/teleop' topic, which will be read by kobuki base. once we know how to control movement through a script and not through manual, we can move on to other automation.

## how?

### step 1: create ros package
always create ros package through catkin.
```
cd ~/catkin_ws/src
catkin_create_pkg ros_straightline std_msgs rospy
```

### step 2: create python script
```
cd cd ros_straightline
mkdir scripts # good practice to keep python scripts in a separate folder
touch straightline.py # dont forget to include #!/usr/bin/env python
chmod -x straightline.py # make it executable
```

### step 3: make & source
need to make, even for python executables.
```
cd ~catkin_ws
catkin_make
source ./devel/setup.bash
```

### step 4: execute
* from terminal 1, do `roslaunch turtlebot_bringup minimal.launch`
* from terminal 2, do `rosrun ros_straightline straightline.py`