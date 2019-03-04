#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

print ""
print "****** Moving the robot in a line in XZ plane ******"
group.clear_pose_targets()
group.stop()
print group.get_current_pose().pose
print ""

rospy.sleep(1)

# First point declaration
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.x = 0.5
pose_target.orientation.y = 0.5
pose_target.orientation.z = -0.5
pose_target.orientation.w = 0.5
pose_target.position.x = 0.00
pose_target.position.y = 0.30
pose_target.position.z = 0.88
group.set_pose_target(pose_target)

movement = group.go(wait=True)
group.stop()
group.clear_pose_targets()

print "====== Point 1/5 ======"
print group.get_current_pose().pose
print ""

rospy.sleep(1)

# Second point declaration
pose_target.position.z = 0.93
group.set_pose_target(pose_target)

movement = group.go(wait=True)
group.stop()
group.clear_pose_targets()

print "====== Point 2/5 ======"
print group.get_current_pose().pose
print ""

rospy.sleep(2)

# Third point declaration
pose_target.position.z = 0.88
group.set_pose_target(pose_target)

movement = group.go(wait=True)
group.stop()
group.clear_pose_targets()

print "====== Point 3/5 ======"
print group.get_current_pose().pose
print ""

rospy.sleep(2)

print "****** Finish drawing a line in the XZ plane ******"

moveit_commander.roscpp_shutdown()

