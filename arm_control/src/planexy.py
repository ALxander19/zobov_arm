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
print "****** Moving the robot in a rectangle in XY plane ******"
group.clear_pose_targets()
group.stop()
print group.get_current_pose().pose
print ""

rospy.sleep(2)

# First point declaration
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.x = 0.707
pose_target.orientation.y = 0.707
pose_target.orientation.z = 0.0
pose_target.orientation.w = 0.0
pose_target.position.x = 0.03
pose_target.position.y = 0.35
pose_target.position.z = 0.80
group.set_pose_target(pose_target)

movement = group.go(wait=True)
group.stop()
group.clear_pose_targets()

print "====== Point 1/5 ======"
print group.get_current_pose().pose
print ""

rospy.sleep(2)

# Second point declaration
pose_target.position.x = -0.03
group.set_pose_target(pose_target)

movement = group.go(wait=True)
group.stop()
group.clear_pose_targets()

print "====== Point 2/5 ======"
print group.get_current_pose().pose
print ""

rospy.sleep(2)

# Third point declaration
pose_target.position.y = 0.30 # = 0.35 - 0.05
group.set_pose_target(pose_target)

movement = group.go(wait=True)
group.stop()
group.clear_pose_targets()

print "====== Point 3/5 ======"
print group.get_current_pose().pose
print ""

rospy.sleep(2)

# Fourth point declaration
pose_target.position.x = 0.03
group.set_pose_target(pose_target)

movement = group.go(wait=True)
group.stop()
group.clear_pose_targets()

print "====== Point 4/5 ======"
print group.get_current_pose().pose
print ""

# Fourth point declaration
pose_target.position.y = 0.35
group.set_pose_target(pose_target)

movement = group.go(wait=True)
group.stop()
group.clear_pose_targets()

print "====== Point 5/5 ======"
print group.get_current_pose().pose
print ""

rospy.sleep(2)

print "****** Finish drawing a rectangle in the XY plane ******"

moveit_commander.roscpp_shutdown()

