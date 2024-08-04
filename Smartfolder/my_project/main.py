import RPi.GPIO as GPIO
import time
import os

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Disable warnings

# Define button pins
buttonPin = 17
buttonPina = 25

# Set up GPIO pins
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Use pull-down resistor
GPIO.setup(buttonPina, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Use pull-down resistor

try:
    while True:
        # Check if either button is pressed
        if GPIO.input(buttonPin) or GPIO.input(buttonPina):
            print("button pressed")
            # Capture image and run email script
            #os.system("fswebcam -r 960x720 -d /dev/video0 /home/pi/my_project/nks.jpg")
            os.system("python /home/pi/my_project/emailscript.py")
        time.sleep(0.1)  # Add a small delay to debounce
except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()
