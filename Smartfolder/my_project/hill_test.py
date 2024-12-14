import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)  # GPIO 17 as input

try:
    while True:
        if GPIO.input(17):  # Check if the input is HIGH (3.3V)
            print("Button Pressed")
        else:
            print("Button Not Pressed")
        time.sleep(0.1)  # Delay for a short time before checking again
except KeyboardInterrupt:
    GPIO.cleanup()
