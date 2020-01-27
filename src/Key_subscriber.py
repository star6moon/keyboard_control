#!/usr/bin/env python

import rospy
from std_msgs.msg import String



def callback(data):
      key = data.data
      # print("{} Sub key : {}".format(rospy.get_caller_id(),key))
      rospy.loginfo("Sub key :%s", data.data) #rospy.get_caller_id()
      if (key == '\x03'):
            print('publisher stop working')

def Key_subscriber():
      rospy.init_node('Key_subscriber',anonymous=True)
      rospy.Subscriber("keyboard", String, callback)

      rospy.spin()

if __name__=='__main__':
      Key_subscriber()


