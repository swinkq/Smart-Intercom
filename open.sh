#!/bin/bash

echo 12 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio12/direction
echo 0 > /sys/class/gpio/gpio12/value

ping -c 1 localhost

echo 12 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio12/direction
echo 1 > /sys/class/gpio/gpio12/value
python /home/pi/led.py
