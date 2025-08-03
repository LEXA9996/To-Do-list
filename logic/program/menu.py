from .read_task import ActiveComletedTaskWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from design.py_design.main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.read_active_task.clicked.connect(self.read_active_task)

    def read_active_task(self):
        window = ActiveComletedTaskWindow()
        window.exec()