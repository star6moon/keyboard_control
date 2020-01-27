#!/usr/bin/env python

import rospy, sys
from std_msgs.msg import String
import numpy as np

key_dict = {
        'w':(  1,   0,   0),
        's':(  0,   0,   0),
        'a':(  0,   1,   0),
        'd':(  0,   0,   1),
      }
speed = 0
steer = 0
key = 0
sp_stack = 1
st_stack = 1
st_count = 0
zero_sp = 0

def callback(data):
    global speed, steer, sp_stack, st_stack, st_count, zero_sp
    key = data.data
    # print("{} Sub key : {}".format(rospy.get_caller_id(),key))
    # rospy.loginfo("Sub key :%s", data.data) #rospy.get_caller_id()

    if key in key_dict.keys():
        sp_rate = 1.3
        if (key_dict[key][0] or key_dict[key][1] or key_dict[key][2]) == 0:
            sp_stack = 1
            zero_sp = 0
        elif key_dict[key][0] == 1:
            sp_stack = key_dict[key][0] * sp_stack * sp_rate + (not(key_dict[key][0])) * sp_stack
            zero_sp = 1

        speed = sp_stack * (key_dict[key][0] or key_dict[key][1] or key_dict[key][2]) * zero_sp

        st_count += -key_dict[key][1] + key_dict[key][2]
        st_stack = (st_count != 0) * (2**(abs(st_count) - 1))
        steer = -(st_count <0) * st_stack + (st_count > 0) * st_stack

    else:
        sp_stack = 1
        speed = 0
        steer = 0
        st_count = 1
        if (key == '\x03'):
            print('publisher stop working')
            

    state = 'speed : {:0.4f} , steer : {:0.4f} '.format(speed, steer)
    print(state)



def Key_subscriber():
    rospy.init_node('car_controller',anonymous=True)
    rospy.Subscriber("keyboard", String, callback)
    rospy.spin()

if __name__=='__main__':

    Key_subscriber()


