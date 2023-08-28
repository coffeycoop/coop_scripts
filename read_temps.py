#!/usr/bin/python

import os
import time
import logging

#Initialize serial data steam 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#Set logging specs
logging.basicConfig(filename='/home/will/python_prog/coop_temp.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

#Instantiate temperature directory paths
probe_1 = '/sys/bus/w1/devices/28-01212e353b07/w1_slave'
probe_2 = '/sys/bus/w1/devices/28-01212f45d8e0/w1_slave'

#Pull the raw data 
def read_temp_raw(x):
    f = open(x, 'r')
    lines = f.readlines()
    f.close()
    return lines

#Parse the temperature data 
def read_temp(x):
    lines = read_temp_raw(x)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(x)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return str(temp_c) + ' C', str(temp_f) + ' F'
	
#Run the program, output data
#while True:
#	print('Probe 1: ' + str(read_temp(probe_1)))
#	print('Probe 2: ' + str(read_temp(probe_2)))	
#	time.sleep(1)

res_1 = str(read_temp(probe_1))
res_2 = str(read_temp(probe_2))

logging.info('%s', res_1)
