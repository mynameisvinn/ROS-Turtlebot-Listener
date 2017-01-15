## using launch files

instead of using roscore + rosrun, you can use launch files.

launch files typically look like this:
```
<launch>
  <node name="talker" pkg="beginner_tutorials" type="pub.py" output="screen"/>
</launch>
```

then, from catkin workspace, do:
```
source ./devel/setup.bash #always source
roslaunch beginner_tutorials pub.launch
```

reference: https://github.com/ros/ros_tutorials/tree/kinetic-devel/rospy_tutorials/001_talker_listener