from create_table.crearte_table import table
from program.menu import menu
from time_page import check_time
import threading

table()
threading.Thread(target=check_time.check_overdue_time, daemon=True).start()
threading.Thread(target=check_time.check_completed_time, daemon=True).start()
menu()
