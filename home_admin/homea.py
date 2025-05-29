from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
from PyQt6.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 590)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 921, 551))
        self.textEdit.setStyleSheet("border-image: url(../image/anhdep.jpg);")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 10, 221, 61))
        self.label.setStyleSheet("QLabel {\n"
"    color: white; \n"
"    font-size: 20px;  \n"
"    font-weight: bold; \n"
"}")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 90, 271, 61))
        self.pushButton.setStyleSheet("QPushButton {\n"
"            background-color: #ffffff;\n"
"            color: #2C3E50;\n"
"            border: 3px solid #ddd;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            padding-left: 10px;\n"
"            transition: padding-left 0.3s ease;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.4);\n"
"            transform: translateY(-2px);\n"
"            border: 3px solid #00CED1;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            transform: translateY(1px);\n"
"            padding-left: 5px;\n"
"            padding-top: 5px;\n"
"        }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/tautau.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(65, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 430, 271, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"            background-color: #ffffff;\n"
"            color: #2C3E50;\n"
"            border: 3px solid #ddd;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            padding-left: 10px;\n"
"            transition: padding-left 0.3s ease;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.4);\n"
"            transform: translateY(-2px);\n"
"            border: 3px solid #00CED1;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            transform: translateY(1px);\n"
"            padding-left: 5px;\n"
"            padding-top: 5px;\n"
"        }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/ghengoi.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(46, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 200, 271, 61))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"            background-color: #ffffff;\n"
"            color: #2C3E50;\n"
"            border: 3px solid #ddd;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            padding-left: 10px;\n"
"            transition: padding-left 0.3s ease;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.4);\n"
"            transform: translateY(-2px);\n"
"            border: 3px solid #00CED1;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            transform: translateY(1px);\n"
"            padding-left: 5px;\n"
"            padding-top: 5px;\n"
"        }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image/toa_toa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(70, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 320, 271, 61))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"            background-color: #ffffff;\n"
"            color: #2C3E50;\n"
"            border: 3px solid #ddd;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            padding-left: 10px;\n"
"            transition: padding-left 0.3s ease;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.4);\n"
"            transform: translateY(-2px);\n"
"            border: 3px solid #00CED1;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            transform: translateY(1px);\n"
"            padding-left: 5px;\n"
"            padding-top: 5px;\n"
"        }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../image/vetau.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(65, 70))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 200, 271, 61))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"            background-color: #ffffff;\n"
"            color: #2C3E50;\n"
"            border: 3px solid #ddd;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            padding-left: 10px;\n"
"            transition: padding-left 0.3s ease;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.4);\n"
"            transform: translateY(-2px);\n"
"            border: 3px solid #00CED1;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            transform: translateY(1px);\n"
"            padding-left: 5px;\n"
"            padding-top: 5px;\n"
"        }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../image/lichtrinh.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(51, 55))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 320, 271, 61))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"            background-color: #ffffff;\n"
"            color: #2C3E50;\n"
"            border: 3px solid #ddd;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            padding-left: 10px;\n"
"            transition: padding-left 0.3s ease;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.4);\n"
"            transform: translateY(-2px);\n"
"            border: 3px solid #00CED1;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            transform: translateY(1px);\n"
"            padding-left: 5px;\n"
"            padding-top: 5px;\n"
"        }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../image/khach_hang.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(48, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 430, 271, 61))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"            background-color: #ffffff;\n"
"            color: #2C3E50;\n"
"            border: 3px solid #ddd;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            padding-left: 10px;\n"
"            transition: padding-left 0.3s ease;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.4);\n"
"            transform: translateY(-2px);\n"
"            border: 3px solid #00CED1;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            transform: translateY(1px);\n"
"            padding-left: 5px;\n"
"            padding-top: 5px;\n"
"        }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../image/chitiet.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(550, 90, 271, 61))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"            background-color: #ffffff;\n"
"            color: #2C3E50;\n"
"            border: 3px solid #ddd;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            padding-left: 10px;\n"
"            transition: padding-left 0.3s ease;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: 6px 6px 12px rgba(0, 0, 0, 0.4);\n"
"            transform: translateY(-2px);\n"
"            border: 3px solid #00CED1;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            background-color:  #ffffff;\n"
"            box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.3);\n"
"            transform: translateY(1px);\n"
"            padding-left: 5px;\n"
"            padding-top: 5px;\n"
"        }")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../image/nhanvien.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(50, 60))
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TRANG CHỦ ADMIN"))
        self.pushButton.setText(_translate("MainWindow", "Quản lí tàu"))
        self.pushButton_2.setText(_translate("MainWindow", "Quản lí ghế ngồi"))
        self.pushButton_3.setText(_translate("MainWindow", "Quản lí toa"))
        self.pushButton_4.setText(_translate("MainWindow", "Quản lí vé tàu"))
        self.pushButton_5.setText(_translate("MainWindow", "Quản lí lịch trình"))
        self.pushButton_6.setText(_translate("MainWindow", "Quản lí khách hàng"))
        self.pushButton_7.setText(_translate("MainWindow", "Quản lí chi tiết lịch trình"))
        self.pushButton_8.setText(_translate("MainWindow", "Quản lí người dùng"))
        self.pushButton.clicked.connect(self.qltau)
        self.pushButton_2.clicked.connect(self.qlghengoi)
        self.pushButton_3.clicked.connect(self.qltoa)
        self.pushButton_4.clicked.connect(self.qlvetau)
        self.pushButton_5.clicked.connect(self.qllichtrinh)
        self.pushButton_6.clicked.connect(self.qlkh)
        self.pushButton_7.clicked.connect(self.qlctlt)
        self.pushButton_8.clicked.connect(self.qlnguoidung)
    def qltau(self):
        try:
            subprocess.run(["python", "../home_admin/Ql_tau.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình: {e}")
    def qlghengoi(self):
        try:
            subprocess.run(["python", "../home_admin/Ql_ghe_ngoi.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình: {e}")
    def qltoa(self):
        try:
            subprocess.run(["python", "../home_admin/Ql_toa.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình: {e}")
    def qlvetau(self):
        try:
            subprocess.run(["python", "../home_admin/Ql_ve.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình: {e}")
    def qllichtrinh(self):
        try:
            subprocess.run(["python", "../home_admin/Ql_lich_trinh.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình: {e}")
    def qlkh(self):
        try:
            subprocess.run(["python", "../home_admin/Ql_ttkh.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình: {e}")
    def qlctlt(self):
        try:
            subprocess.run(["python", "../home_admin/Ql_ctlt.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình: {e}")
    def qlnguoidung(self):
        try:
            subprocess.run(["python", "../home_admin/Ql_nguoi_dung.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình: {e}")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
