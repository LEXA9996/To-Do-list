from .read_task import ActiveComletedTaskWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from design.py_design.main_window import Ui_MainWindow
from .read_completed_task import ComletedTask
from .add_task import AddTaskWindow
from .mark_completed_task import MarkCompletedTask
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.read_active_task.clicked.connect(self.read_active_task)
        self.ui.read_completed_task.clicked.connect(self.read_completed_task)
        self.ui.add_task.clicked.connect(self.add_task)
        self.ui.completed_task.clicked.connect(self.completed_task)

    def read_active_task(self):
        window = ActiveComletedTaskWindow()
        window.exec()
    def read_completed_task(self):
        window = ComletedTask()
        window.exec()
    def add_task(self):
        window = AddTaskWindow()
        window.exec()
    def completed_task(self):
        window = MarkCompletedTask()
        window.exec()