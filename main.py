from mainwindow import Ui_MainWindow
import mainwindow
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QMainWindow()
    main_window = mainwindow.Ui_MainWindow()
    main_window.setupUi(w)
    w.show()

    sys.exit(app.exec())
