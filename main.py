from logic.create_table.crearte_table import table
from logic.time_page import check_time
import threading, sys
from PySide6.QtWidgets import QApplication, QMainWindow
from logic.program.menu import MainWindow
table()
threading.Thread(target=check_time.check_overdue_time, daemon=True).start()
threading.Thread(target=check_time.check_completed_time, daemon=True).start()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())