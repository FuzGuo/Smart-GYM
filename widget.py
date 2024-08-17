# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget
import PySide6, os
from PySide6.QtCore import Qt

from main_window.NavigationWidget import Window
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from loginUi import Ui_Form


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框窗口标志
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        self.setWindowIcon(QIcon("resource/icons/dumbbell-svgrepo-com.svg"))

        self.ui.pushButton_14.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton_16.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton_20.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton_3.clicked.connect(lambda: self.handleLoginWindow())

    def handleLoginWindow(self):
        if self.ui.handleLogin():
            mainwindow = Window(self.ui.user[0])
            mainwindow.show()
            # mainwindow.user =
            self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()
        elif event.button() == Qt.RightButton:
            pass

    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.moving = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    # widget.setWindowFlag()
    widget.show()
    sys.exit(app.exec())
