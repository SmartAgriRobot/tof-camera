import threading
import time
import serial

import functools
import operator

import cv2
from tof_lib import *

ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=250000,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

cmd_getdeviceinfo = b'\x5A\x77\xFF\x02\x00\x10\x00\x12'
cmd_str = cmd_getdeviceinfo

ser.write(cmd_str)
s = ser.read(13)

cmd_get3Dframe = b'\x5A\x77\xFF\x02\x00\x08\x00\x0A'
cmd_str = cmd_get3Dframe

ser.write(cmd_str)

thread = threading.Thread(target=read_from_port, args=(ser,))
thread.start()

while True:
	time.sleep(1)
	if fExit:
		break

cv2.destroyAllWindows()
cmd_stopDevice = b'\x5A\x77\xFF\x02\x00\x02\x00\x00'
cmd_str = cmd_stopDevice
ser.write(cmd_str)
ser.close()