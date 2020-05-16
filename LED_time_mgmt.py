#!/usr/bin/python

## LIBRARIES, simple list
import datetime
import time
import os
import logging

## GLOBAL VARS
begin_time = datetime.time(8,0)
end_time = datetime.time(18,0)
usb_path = "/sys/bus/usb/drivers/usb/"
LED_STATUS = "OFF"

logging.basicConfig(filename="/home/pi/Programs/log/LED_time_mgmt.log", filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info('Program Starting')

## Checking if it's the right time
def is_time_between(begin_time, end_time, check_time=None):
  check_time = check_time or datetime.datetime.now().time()
  logging.info("Checking the time now", check_time)
  print("checking the time - is ", check_time, "between ", begin_time, " and ", end_time, "?")
  if begin_time < end_time:
    return check_time >= begin_time and check_time <= end_time
  else: #for cross-midnight situations
    return check_time >= begin_time or check_time <= end_time
  

# Turning LED on/off
def turn_on():
  cmd = "echo '1-1' | sudo tee " + usb_path + "bind"
  print("cmd = ", cmd)
  os.system(cmd)
  
def turn_off():
  cmd = "echo '1-1' | sudo tee " + usb_path + "unbind"
  print("cmd = ", cmd)
  os.system(cmd)


## Now we start MAIN()

while(True):
  if is_time_between(begin_time, end_time) and LED_STATUS == "OFF":
    print("Turning LED to ON")
    turn_on()
    LED_STATUS = "ON"
  elif is_time_between(begin_time, end_time) and LED_STATUS == "ON":
    print("LED is already ON - no action")
  elif not is_time_between(begin_time, end_time) and LED_STATUS == "ON":
    print("Turning LED to OFF")
    turn_off()
    LED_STATUS = "OFF"
  elif not is_time_between(begin_time, end_time) and LED_STATUS == "OFF":
    print("LED is already OFF - no action")
  else:
    print("how the HELL did we get here?!?")
  time.sleep(300)

## end of program
