#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from datetime import datetime

def callback(data):
	tme=datetime.now()
	#msg="%s %s:%s:%s"%		(data.data,tme.hour,tme.minute,tme.second)
	#rospy.loginfo(msg)
	rospy.loginfo(rospy.get_name() + " I take message: %s %s:%s:%s:",data.data, tme.hour, tme.minute, 		tme.second)

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
