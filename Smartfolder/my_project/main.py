import RPi.GPIO as GPIO
import time
import os
import emailscript
import sms_script
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

            image_path = "/home/pi/my_project/visitor.jpg"
            os.system(f"libcamera-still -o {image_path}")
            
            print(f"Image saved at {image_path}")

            # Send SMS with image
            sms_script.send_sms_with_image(image_path)

            #emailscript.send_email_route()
        time.sleep(0.1)  # Add a small delay to debounce
except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()
