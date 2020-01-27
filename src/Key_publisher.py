#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import sys, select, tty, termios


def Key_publisher():
    pub = rospy.Publisher('keyboard',String,queue_size=10)
    rospy.init_node('Key_publisher', anonymous = True)
    rate = rospy.Rate(10) #10hz
    while not rospy.is_shutdown():
        key = getKey()
        if key != '\x03' and key != 0:  # '\x03' is ctrl + c
            # print(key)
            key_str = "Pub key : %s" % key  # , rospy.get_time()
            rospy.loginfo(key_str)
        else:
            print('stop key publisher')
            pub.publish(key)
            break

        pub.publish(key)
        rate.sleep()

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__=='__main__':
    settings = termios.tcgetattr(sys.stdin)
    try:
        Key_publisher()
    except rospy.ROSInterruptException:
        pass


