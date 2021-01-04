#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	r = rospy.Rate(1)

	while not rospy.is_shutdown():
		#name = input()
		str = "Matveev K.A. %s"%rospy.get_time()
		rospy.loginfo(str)	 
    		pub.publish(String(str))
    		r.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass

