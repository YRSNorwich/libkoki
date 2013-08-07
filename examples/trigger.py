#!/env/python

import subprocess
import os.path
import io
import serial

#ser = serial.Serial("/dev/ttyACM0",9600, timeout= 2)

def invoke_subprocess(bufsize):
    #return subprocess.Popen(os.path.join(os.getcwd(), 'realtime_text'), shell=True, stdout=subprocess.PIPE, bufsize=bufsize)
    return subprocess.Popen('./firecontrol_eyeball', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=bufsize)

 
def io_open():
    p = invoke_subprocess(1)
    for line in io.open(p.stdout.fileno()):
        yield line.rstrip('\n')


while True:
	print "start"
	counter = 0
	for line in io_open():
		if not '0' in line:
			counter +=1
			if counter == 5:
				break
		else:
			counter = 0
			print counter

	print "fire!!!!!"

#ser.write("1")
    	

    	
