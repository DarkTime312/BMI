from PySide6.QtWidgets import QApplication
import sys

from controller import BmiController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BmiController()
    window.view.show()
    sys.exit(app.exec())
