"""

Pinary-Lights

Python Script to evaulate decimal number to binary and light up corresponding
LEDs controlled by a Raspberry Pi 2 GPIO interface.

This script uses broadcom numbering for the GPIO pins and the gpiozero library.

Copyright <2016> <Stephen Spence>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from gpiozero import LED
from PyQt5 import QtGui
import sys
import time
import UIlights

class BinaryLights(QtGui, QMainWindow, testUI.Ui_MainWindow):
    """docstring for """
    def __init__(self, parent=None):
        super(BinaryLights, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.PinaryLights)
        self.le =QLineEdit()

    def PinaryLights(self):

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

        x = self.le.text()

        #while x < 1 or x > 255:

            #x = int(input ("Enter a Number between 1 and 255:"))

        for n in range (0, 8):
            rem = x%2
            if rem == 1:
                Bits[n].on()
            x = x // 2

        time.sleep(5)
        for n in range (0, 8):
            Bits[n].off()
        pass

def main():
    app = QtGui.QApplication(sys.argv)
    form = BinaryLights()
    form.show()
    app.exec_()

if _name_ == '_main_':
    main()
