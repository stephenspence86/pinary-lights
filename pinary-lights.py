"""

Pinary-Lights

Python Script to evaulate decimal number to binary and light up corresponding
LEDs controlled by a Raspberry Pi 2 GPIO interface.

This script uses broadcom numbering for the GPIO pins and the gpiozero library.
"""

from gpiozero import LED
from signal import pause


DecNumber = input("Enter a Number between 1 and 255: ")

    if DecNumber < 1 or > 255
        print ("Pick a Number between 1 and 255: ")
        DecNumber = input
        else # Modulo division for DecNumber to BinNumber

    if bit1 == 1
        LED(6).on
        else
        LED(6).off
