#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import fnmatch
import os

def indir_scanner():
	pub = rospy.Publisher('filename',String,queue_size=10)
	rospy.init_node('indir_file_pub', anonymous=True)

	r = rospy.Rate(10)

	while not rospy.is_shutdown():
		print 'Input scan directory path'
		dir_path = raw_input()
		print 'Input scan extension'
		file_ext = raw_input()
		for file in os.listdir(dir_path):
			if fnmatch.fnmatch(file, '*'+file_ext):
				rospy.loginfo(file)
				pub.publish(file)
				r.sleep()

if __name__ == '__main__':
	try:
		indir_scanner()
	except rospy.ROSInterruptException: pass




