##代码的主要功能是力信息采集及信号滤波处理，最好添加重力补偿部分的力曲线。
import rospy
import rtde_receive
import rtde_control
import time
import argparse
import sys
import csv
from std_msgs.msg import Float64MultiArray
from scipy import signal
import numpy as np
fs=250

fn=40
wn=(fn/fs)   # 2*(fn/fs[0])
b, a = signal.butter(8, [0.2,0.8], 'bandpass')   


rtde_r = rtde_receive.RTDEReceiveInterface("192.168.3.101")
rtde_c=rtde_control.RTDEControlInterface("192.168.3.101")
Read_flag=True



i = 0
dt=0.05
# try:
#     while Read_flag:
#         start = time.time()
#         force_data=rtde_r.getActualTCPForce()
#         with open("force_static.csv","a",newline='') as g:
#                     writer1 = csv.writer(g)
#                     writer1.writerow(force_data)
#         end = time.time()
#         duration = end - start

#         if duration < dt:
#             time.sleep(dt - duration)
#         i += 1
# except KeyboardInterrupt:
#     print(i)
#     Read_flag=False
#     print("\nData recording stopped.")

def talker():
    pub = rospy.Publisher('force', Float64MultiArray, queue_size=1)
    pub_seg = rospy.Publisher('force_seg', Float64MultiArray, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        force_data=Float64MultiArray()
        sig_force=Float64MultiArray()
        rtde_c.zeroFtSensor()
        force_data.data=rtde_r.getActualTCPForce()
        print(force_data.data)
        with open("滤波前力信息.csv","a",newline='') as g:
            writer1 = csv.writer(g)
            writer1.writerow(force_data.data)
        print("*******************************")
        
        sig_data=np.array(force_data.data)
        # print(sig_data)
        sig_ecg = signal.filtfilt(b, a, sig_data,padlen=0)
        sig_force.data=sig_ecg
        print(sig_ecg)
        with open("滤波后力信息.csv","a",newline='') as g:
            writer1 = csv.writer(g)
            writer1.writerow(sig_ecg)
        print("***********************************")
        pub.publish(force_data)
        pub_seg.publish(sig_force)
        rate.sleep()
if __name__ == '__main__':
    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


