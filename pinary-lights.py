"""

Pinary-Lights

Python Script to evaulate decimal number to binary and light up corresponding
LEDs controlled by a Raspberry Pi 2 GPIO interface.

This script uses broadcom numbering for the GPIO pins and the gpiozero library.
"""

from gpiozero import LED
import time

Bit1 = LED(17)
Bit2 = LED(27)
Bit3 = LED(22)
Bit4 = LED(5)
Bit5 = LED(6)
Bit6 = LED(13)
Bit7 = LED(19)
Bit8 = LED(26)

Bits = [Bit1, Bit2, Bit3, Bit4, Bit5, Bit6, Bit7, Bit8]

for n in range (0, 8):
    Bits[n].off()

x = int(input("Enter a Number between 1 and 255: "))

while x < 1 or x > 255:

    x = int(input ("Enter a Number between 1 and 255:"))

for n in range (0, 8):
    rem = x%2
    if rem == 1:
        Bits[n].on()
    x = x // 2

time.sleep(5)
for n in range (0, 8):
    Bits[n].off()
