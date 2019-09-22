import RPi.GPIO as GPIO
import time
pingpio=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pingpio, GPIO.OUT)
GPIO.output(pingpio, GPIO.LOW)
time.sleep(5)
GPIO.output(pingpio, GPIO.HIGH)
