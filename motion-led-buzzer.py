import RPi.GPIO as GPIO
import time

PIR_PIN = 17
LED_PIN = 27
BUZZER_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

print("Warming up PIR sensor")
time.sleep(30)
print("System ready. Watching for motion")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected! Alert triggered.")
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(5)  # Alert duration
            GPIO.output(LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            print("Alert cleared. Waiting before resuming.")
            time.sleep(2)
        else:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    GPIO.cleanup()
