import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from widget.ui.bgeffect import BgEffect

app = QApplication(sys.argv)
window = QWidget()

window.setStyleSheet("background-color: #ffe1f9;")
window.resize(720, 480)

#BgEffect(window)

#window.setAttribute(Qt.WA_TranslucentBackground)

window.show()

sys.exit(app.exec_())