from logic.create_table.crearte_table import table
from logic.program.menu import menu
from logic.time_page import check_time
import threading, sys
from PySide6.QtWidgets import QApplication, QMainWindow
from design.py_design.main_window import Ui_MainWindow

table()
threading.Thread(target=check_time.check_overdue_time, daemon=True).start()
threading.Thread(target=check_time.check_completed_time, daemon=True).start()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())