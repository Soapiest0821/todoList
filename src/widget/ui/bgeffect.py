import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class BgEffect(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.enableBlur()

    def enableBlur(self):
        hwnd = self.parent().winId().__int__()
        