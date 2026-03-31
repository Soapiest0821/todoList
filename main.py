import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 350)
window.move(1120, 335)
window.show()        # 10초 = 10000ms

sys.exit(app.exec_())