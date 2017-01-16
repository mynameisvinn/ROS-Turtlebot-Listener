# barnacle

## what is this?
this is the central catkin workspace for barnacle's apps.

## requirements
building ros on arm is not fun, but here it is:

* [grinch kernel](http://wiki.ros.org/NvidiaJetsonTK1)
* [ROS for tk1](https://github.com/jetsonhacks/installROS)
* [ROS indigo](http://wiki.ros.org/indigo/Installation/Ubuntu)
* [astra ros camera](https://github.com/orbbec/ros_astra_camera)
* [astra launch](https://github.com/orbbec/ros_astra_launch)
* [cuda 6.5](https://gist.github.com/jetsonhacks/6da905e0675dcb5cba6f)
* [ros caffe](https://github.com/mynameisvinn/ros_caffe)

## how do i build from source?
```
git clone [SOME_REPO]
cd catkin_ws
source ./devel/setup.sh
catkin_make
```

## helpful links
* [artificialintelligence missing instructions](http://www.artificialhumancompanions.com/)