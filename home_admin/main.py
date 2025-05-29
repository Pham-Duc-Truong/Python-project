#import
from PyQt6 import QtGui, QtCore, QtWidgets
import sys
from matplotlib.backends.backend_qt import MainWindow
import login,home_admin
import pymysql
#xuly
ui=''
app=QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def login():
    global ui
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_login.clicked.connect()
    MainWindow.show()

login()
sys.exit(app.exec())

