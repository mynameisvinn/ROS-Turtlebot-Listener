# ros image_listener

create a subscriber that grabs images from the camera and save it. this is a good example of creating packages in catkin.

## create a catkin workspace

```
cd ~/catkin_ws/src
catkin_init_workspace
cd ..
catkin_make
source devel/setup.bash
```
find more information at this [wiki](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

## create a catkin package
```
cd ~/catkin_ws/src
catkin_create_pkg ros_image std_msgs rospy roscpp
```
find more information at this [wiki](http://wiki.ros.org/catkin/Tutorials/CreatingPackage)

## create scripts and make it executable
```
cd ~/catkin_ws/src/ros_image
mkdir scripts # for python scripts
cd scripts
```
create your python in the `scripts` folder. dont forget to make the script executable by doing `chmod +x script_name.py`

in this case, the image_listener.py was inspired from http://answers.ros.org/question/210294/ros-python-save-snapshot-from-camera/

## run script
```
roslaunch turtlebot_bringup 3dsensor.launch
rosrun ros_image image_listener.py
```
script should subscribe to topic `camera/rgb/image_raw` and start saving images. to view images, do `$ eog camera_image.jpeg`

