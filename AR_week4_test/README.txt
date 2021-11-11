Student Name: Joshua Colletta


Install:

Assuming you have a ~/catkin_ws:

1. Copy and extract the zip inside ~/catkin_ws/src
2. cd ..
2. run 'rosdep init'
3. run 'rosdep update'
4. run 'rosdep install --from-paths ./src --ignore-packages-from-source --rosdistro melodic -y'
5. run 'catkin_make install'
6. run 'source devel/setup.bash' (bash.rc is configured but has trouble the first time around)
7. run 'roslaunch ~/catkin_ws/src/AR_week4_test/launch/cubic_traj_gen.launch'

If you dont have a catkin_ws yet:
1. mkdir -p ~/catkin_ws/src
2. cd ~/catkin_ws/
3. echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
4. source ~/.bashrc
5. catkin_make
(catkin env now ready)

Development Environment: 
LAPTOP
Windows 10 Pro/64Bit
Ubuntu 20.4(LTS)/64Bit
Python Version: 3.7.0 & 3.7.5 

PI (3B+) (Passed Testing)
Ubuntu 18.04.2 / armfh instruction set for arm7 proc /
Python Version:3.7.5
ROS Version: Melodic
Running Headless, ssh over local network.

WSL (V1) ubunutu 18.04
python version 2.7 and 3.6
(Passed Testing)





