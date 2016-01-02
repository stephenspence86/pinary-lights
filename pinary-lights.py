"""

Pinary-Lights

Python Script to evaulate decimal number to binary and light up corresponding
LEDs controlled by a Raspberry Pi 2 GPIO interface.

This script uses broadcom numbering for the GPIO pins and the gpiozero library. 
"""

from gpiozero import LED
from signal import pause


x = input("Enter a Number between 1 and 255: ")

