import RPi.GPIO as GPIO
import time
import sys
import argparse

#Set up help notices and program inputs
parser = argparse.ArgumentParser(description="Opens or closes chicken coop door taking input commands to either open or shut and for how long to turn the motor.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-o", "--open", action="store_true", help="Opens chicken coop door")
group.add_argument("-c", "--close", action="store_true", help="Closes chicken coop door")
parser.add_argument("time", type=int, help="Time in seconds to operate motor")
args = parser.parse_args()

#Configure to use board pin numbers
try:
    GPIO.setmode(GPIO.BOARD)
except:
    print("Could not set up board mode!")

#Configure physical pins
try:
    cw = 5
    ccw = 3
    pwm = 11
    GPIO.setup(cw, GPIO.OUT)
    GPIO.setup(ccw, GPIO.OUT)
#    GPIO.setup(pwm, GPIO.OUT)
except:
    print("Could not set up pins properly!")

#Set values for desired operation
try:
    sec = int(sys.argv[2])
except:
   print("There was an issue determining the time!")

try:
    flag = sys.argv[1]
except:
    print("There was an issue determining the desired operation!")

#Apply brake
GPIO.output(cw, GPIO.LOW)
GPIO.output(ccw, GPIO.LOW)


#Define full speed turns
def close(x):
  GPIO.output(cw, GPIO.HIGH)
  GPIO.output(ccw, GPIO.LOW)
  time.sleep(x)
  GPIO.output(cw, GPIO.LOW)

def open(x):
  GPIO.output(ccw, GPIO.HIGH)
  GPIO.output(cw, GPIO.LOW)
  time.sleep(x)
  GPIO.output(ccw, GPIO.LOW)

# Activate motor
try:
    if flag == "-o":
        print("Opening for "+ str(sec) + " seconds...")
        open(sec)
    elif flag == "-c":
        print("Closing for "+ str(sec) + " seconds...")
	close(sec)
except:
    print("There was a logic issue causing the door not to move!")

# Reset GPIO Pins
finally:
    print("Task complete.")
    GPIO.cleanup()

## END OF PROGRAM





## PWM code if needed...
#Create PWM instance
#p=GPIO.PWM(pwm,20)
#GPIO.output(cw, GPIO.HIGH)
#p.start(100)
#time.sleep(3)
#p.ChangeDutyCycle(25)
#time.sleep(3)
#p.stop()
