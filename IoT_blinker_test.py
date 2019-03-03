import RPi.GPIO as GPIO
import time

print ("hi, starting now")

#initializes pin counting convention
GPIO.setmode(GPIO.BOARD)

pin_var = 12

# we'll use IO pin #12 for this test
GPIO.setup(pin_var, GPIO.OUT)

counter_limit = 20
for x in range(counter_limit):
    GPIO.output(pin_var, True)
    time.sleep(1)
    print("OFF")
    GPIO.output(pin_var, False)
    time.sleep(1)
    print("ON")
    print("iterations left = ", counter_limit - x)

# cleaning up usage of ports
GPIO.cleanup()
    
print ("hi again, exiting blinker test and clearing ports")


