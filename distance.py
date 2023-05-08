import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN)

pi_pwm = GPIO.PWM(12, 50)
pi_pwm.start(0)

motor_powers = []

try:
    while True:
        GPIO.output(7, GPIO.LOW)
        time.sleep(0.000005)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(7, GPIO.LOW)

        while GPIO.input(11) == 0:
            start = time.time()

        while GPIO.input(11) == 1:
            stop = time.time()

        total_time = stop - start

        distance = (total_time * 34300) / 2

        #max distance is about 65

        motor_power = ((180 / 55) * distance)/18 + 2
        if motor_power > 100:
            motor_power = 100
        if motor_power < 0:
            motor_power = 0

        # Smoothing function
        # Keep only 20 measurements, then take the mean measure to set value
        motor_powers.append(motor_power)
        if len(motor_powers) > 20:
            motor_powers.pop(0)
            pi_pwm.ChangeDutyCycle(sum(motor_powers) / len(motor_powers))




except KeyboardInterrupt:
    GPIO.cleanup()


