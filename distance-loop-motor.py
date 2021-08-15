import time, motor28bjy as motor, hcsr04, kintone, RPi.GPIO as GPIO
from kintone import getCurrentTimeStamp

triggerPin = 14
echoPin = 23
ControlPin = [12,16,20,21]

GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

while(True):
    try:
        distance = hcsr04.getDistance(triggerPin, echoPin)
        # print(getCurrentTimeStamp())

        distance = distance or 0

        if 2 <= distance < 20: 
            motor.rotate(1, ControlPin)
            print("Turning clockwise: Distance (cm): " + str(distance))
        elif 20 <= distance < 40:
            motor.rotate(0, ControlPin)
            print("Turning counter-clockwise: Distance (cm): " + str(distance))
        else:
            time.sleep(0.1)

    except KeyboardInterrupt:
        break

# Write your program above this line
GPIO.cleanup()
