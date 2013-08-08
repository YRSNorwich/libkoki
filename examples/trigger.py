#!/env/python

import subprocess
import os.path
import sys
import io
import serial
from tested.robot import Robot

#ser = serial.Serial("/dev/ttyACM0",9600, timeout= 2)

def invoke_subprocess(bufsize):
    #return subprocess.Popen(os.path.join(os.getcwd(), 'realtime_text'), shell=True, stdout=subprocess.PIPE, bufsize=bufsize)
    return subprocess.Popen('./firecontrol_eyeball', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=bufsize)

 
def io_open():
    proc = invoke_subprocess(0)
    for line in io.open(proc.stdout.fileno()):
        yield line.rstrip('\n')

R = Robot()
print "start"
ready = True
marker_count = 0
absent_count = 0
reps_required = 10

try:
    for line in io_open():
        if not '0' in line:
            marker_count +=1
            if (marker_count >= reps_required) and (ready == True):
                ready = False
                print "Fire!!!"
                #R.servos[0].angle = 76
                marker_count = 0
            else:
                pass
        elif '0' in line:
            absent_count +=1
            if absent_count >= reps_required and ready == False:
                ready = True
                absent_count = 0
                print "Reset"
                R.servos[0].angle = 4

except (KeyboardInterrupt):
    sys.exit()