import os
import sys
import psycopg2

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QMainWindow

from src.interface import MainWindow
from src.interface import Menu_2

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()

        # connecting to database
        db = psycopg2.connect(dbname='cs421', user='cs421g29', host='comp421.cs.mcgill.ca', password='spinBike4!')
        cursor = db.cursor()

        # convert ui file to python file
        #os.system('pyuic5 ./../UI/main.ui -o interface/MainWindow.py')
        self.window = QMainWindow()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        # Menu 2
        # Menu_2.menu_2(self.ui, db)


app = QApplication(sys.argv)

w = AppWindow()
sys.exit(app.exec_())