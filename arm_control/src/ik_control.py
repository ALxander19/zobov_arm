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

print "****** Moving from position ******"
print group.get_current_pose().pose
print ""

rospy.sleep(1)

pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.x = 0.5
pose_target.orientation.y = 0.5
pose_target.orientation.z = -0.5
pose_target.orientation.w = 0.5
pose_target.position.x = 0.00
pose_target.position.y = 0.25
pose_target.position.z = 0.88
group.set_pose_target(pose_target)

# For z = 0.80
# x = -0.03 and y = 0.30 valid?
# x = -0.03 and y = 0.35 valid!

# acepted position x=0.0, y= 0.35, z = 0.95 orientation w = 1.0 up gripper
# like home position x=0.0, y= 0.35, z = 0.95 orientation x = 0.707, w = 0.707 horizontal gripper
# position x=0.0, y= 0.35, z = 0.95 orientation x = 1, w = 0 pick up position

plan = group.plan()

rospy.sleep(1)

movement = group.go(wait=True)
group.stop()
group.clear_pose_targets()

rospy.sleep(1)

print "====== Current Pose ======"
print group.get_current_pose().pose
print ""

moveit_commander.roscpp_shutdown()

