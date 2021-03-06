# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/stealth/rosfuerte_workspace/ardrone_test

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/stealth/rosfuerte_workspace/ardrone_test/build

# Utility rule file for ROSBUILD_gensrv_py.

# Include the progress variables for this target.
include CMakeFiles/ROSBUILD_gensrv_py.dir/progress.make

CMakeFiles/ROSBUILD_gensrv_py: ../src/ardrone_test/srv/__init__.py

../src/ardrone_test/srv/__init__.py: ../src/ardrone_test/srv/_AddTwoInts.py
	$(CMAKE_COMMAND) -E cmake_progress_report /home/stealth/rosfuerte_workspace/ardrone_test/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../src/ardrone_test/srv/__init__.py"
	/opt/ros/fuerte/share/rospy/rosbuild/scripts/gensrv_py.py --initpy /home/stealth/rosfuerte_workspace/ardrone_test/srv/AddTwoInts.srv

../src/ardrone_test/srv/_AddTwoInts.py: ../srv/AddTwoInts.srv
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/rospy/rosbuild/scripts/gensrv_py.py
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/roslib/bin/gendeps
../src/ardrone_test/srv/_AddTwoInts.py: ../manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/roslang/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/roscpp/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/geometry_msgs/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/sensor_msgs/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/ros/core/rosbuild/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/roslib/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/rosconsole/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/pluginlib/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/message_filters/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/image_common/image_transport/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/std_srvs/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/bullet/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/geometry/angles/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/rospy/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/rostest/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/roswtf/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/geometry/tf/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/common_rosdeps/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/image_common/camera_calibration_parsers/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/image_common/camera_info_manager/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /home/stealth/rosfuerte_workspace/ardrone_autonomy/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/share/std_msgs/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/vision_opencv/opencv2/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/vision_opencv/cv_bridge/manifest.xml
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/geometry/tf/msg_gen/generated
../src/ardrone_test/srv/_AddTwoInts.py: /opt/ros/fuerte/stacks/geometry/tf/srv_gen/generated
../src/ardrone_test/srv/_AddTwoInts.py: /home/stealth/rosfuerte_workspace/ardrone_autonomy/msg_gen/generated
../src/ardrone_test/srv/_AddTwoInts.py: /home/stealth/rosfuerte_workspace/ardrone_autonomy/srv_gen/generated
	$(CMAKE_COMMAND) -E cmake_progress_report /home/stealth/rosfuerte_workspace/ardrone_test/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating ../src/ardrone_test/srv/_AddTwoInts.py"
	/opt/ros/fuerte/share/rospy/rosbuild/scripts/gensrv_py.py --noinitpy /home/stealth/rosfuerte_workspace/ardrone_test/srv/AddTwoInts.srv

ROSBUILD_gensrv_py: CMakeFiles/ROSBUILD_gensrv_py
ROSBUILD_gensrv_py: ../src/ardrone_test/srv/__init__.py
ROSBUILD_gensrv_py: ../src/ardrone_test/srv/_AddTwoInts.py
ROSBUILD_gensrv_py: CMakeFiles/ROSBUILD_gensrv_py.dir/build.make
.PHONY : ROSBUILD_gensrv_py

# Rule to build all files generated by this target.
CMakeFiles/ROSBUILD_gensrv_py.dir/build: ROSBUILD_gensrv_py
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/build

CMakeFiles/ROSBUILD_gensrv_py.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean.cmake
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/clean

CMakeFiles/ROSBUILD_gensrv_py.dir/depend:
	cd /home/stealth/rosfuerte_workspace/ardrone_test/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/stealth/rosfuerte_workspace/ardrone_test /home/stealth/rosfuerte_workspace/ardrone_test /home/stealth/rosfuerte_workspace/ardrone_test/build /home/stealth/rosfuerte_workspace/ardrone_test/build /home/stealth/rosfuerte_workspace/ardrone_test/build/CMakeFiles/ROSBUILD_gensrv_py.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/ROSBUILD_gensrv_py.dir/depend

