sudo apt install software-properties-common apt-transport-https wget gpg -y

wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg

sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/

sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

rm -f packages.microsoft.gpg

sudo apt update

sudo apt install code -y

code
-----------------------
estas en el codigo
<exec_depend>slam_toolbox</exec_depend>
<exec_depend>launch</exec_depend>
<exec_depend>launch_ros</exec_depend>
<exec_depend>ament_index_python</exec_depend> <!-- lo usas por get_package_share_directory -->


<buildtool_depend>ament_python</buildtool_depend>

------------------
nodo slam ->>
sudo apt update
sudo apt install ros-jazzy-slam-toolbox
----
sudo apt install ros-jazzy-rplidar-ros
ros2 launch rplidar_ros rplidar.launch.py

