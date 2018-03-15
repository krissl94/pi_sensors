#!/usr/bin/env python
# Led blinks (0.7 second on and 0.3 second off)
# Led connected to GPIO_GEN0 (pin 7) and GND (pin 9) with 560 Ohm Resistor
# Switch connected to GPIO_GEN0 (pin 7) and GND (pin 9) with 1K Resistor
# Input polling 10 times per second
# microHenri 2012-10-14

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
RED_LED = 4
SW1 = 4                                                    # Switch on same port as LED

while True:
    for x in range(10):
        GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Port is input with pullup
        input_value = GPIO.input(SW1)                      # Read input port
        print ("Input is %s" % input_value)
        GPIO.setup(RED_LED, GPIO.OUT)                      # Port is output
        if x < 7: GPIO.output(RED_LED, True)               # LED on
        else: GPIO.output(RED_LED,False)                   # LED off
        time.sleep(0.1)

