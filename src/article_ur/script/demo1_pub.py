import rospy
import rtde_receive
import time
import argparse
import sys
import csv
rtde_r = rtde_receive.RTDEReceiveInterface("192.168.3.101")
Read_flag=True



i = 0
dt=0.001
try:
    while Read_flag:
        start = time.time()
        force_data=rtde_r.getActualTCPForce()
        with open("force_static.csv","a",newline='') as g:
                    writer1 = csv.writer(g)
                    writer1.writerow(force_data)
        end = time.time()
        duration = end - start

        if duration < dt:
            time.sleep(dt - duration)
        i += 1
        

except KeyboardInterrupt:
    print(i)
    Read_flag=False
    print("\nData recording stopped.")