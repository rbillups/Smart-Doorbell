import RPi.GPIO as GPIO
import time
import os
import telebot  # Import the correct module

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define button pins
buttonPin = 17
buttonPina = 25

# Set up GPIO pins
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buttonPina, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(buttonPin) or GPIO.input(buttonPina):
            print("Button pressed")
            image_path = "/home/pi/my_project/visitor.jpg"
            os.system(f"libcamera-still -o {image_path}")
            print(f"Image saved at {image_path}")

            telebot.initializeBot()  # Call the bot initialization
            telebot.handle_button_press(image_path)
            
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
