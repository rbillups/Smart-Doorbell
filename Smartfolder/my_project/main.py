import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
#buttonPin = 4  #for smart lock
buttonPina = 25

buttonPin = 17
#buttonPin = 18
#buttonPin =26
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)
GPIO.setup(buttonPina,GPIO.IN)
#GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    #assuming the script to call is long enough we can ignore bouncing
   # if (GPIO.input(buttonPin)):
    if (GPIO.input(buttonPin) or GPIO.input(buttonPina) ):
        print("button pressed")
        #this is the script that will be called (as root)
        os.system("fswebcam -r 960x720 -d /dev/video0 /home/pi/my_project/nks.jpg")
        os.system("python /home/pi/my_project/emailscript.py")
