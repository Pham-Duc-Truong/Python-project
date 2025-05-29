
from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 374)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(350, 0, 351, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(100, 0, 161, 61))
        self.label.setStyleSheet("QLabel {\n"
"    font-family: \'Segoe UI\', Arial;\n"
"    font-size: 23px;\n"
"    font-weight: bold;\n"
"    color: #2C3E50;\n"
"}")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.dang_nhap = QtWidgets.QLineEdit(parent=self.frame)
        self.dang_nhap.setGeometry(QtCore.QRect(80, 80, 261, 41))
        self.dang_nhap.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #f9f9f9;\n"
"    selection-background-color: #f39c12;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #ffffff;\n"
"}")
        self.dang_nhap.setText("")
        self.dang_nhap.setObjectName("dang_nhap")
        self.mat_khau = QtWidgets.QLineEdit(parent=self.frame)
        self.mat_khau.setGeometry(QtCore.QRect(80, 160, 261, 41))
        self.mat_khau.setStyleSheet("QLineEdit {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    background-color: #f9f9f9;\n"
"    selection-background-color: #f39c12;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #4CAF50;\n"
"    background-color: #ffffff;\n"
"}")
        self.mat_khau.setText("")
        self.mat_khau.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.mat_khau.setObjectName("mat_khau")
        self.btn_back = QtWidgets.QPushButton(parent=self.frame)
        self.btn_back.setGeometry(QtCore.QRect(210, 250, 121, 41))
        self.btn_back.setStyleSheet("QPushButton {\n"
"    background-color: #F44336; \n"
"    color: white;\n"
"    border: 2px solid #F44336;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D32F2F;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #B71C1C; \n"
"}")
        self.btn_back.setObjectName("btn_back")
        self.btn_login = QtWidgets.QPushButton(parent=self.frame)
        self.btn_login.setGeometry(QtCore.QRect(40, 250, 121, 41))
        self.btn_login.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: 2px solid #4CAF50;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #388E3C;\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 55, 41))
        self.label_3.setStyleSheet("border-image: url(../image/khach_hang.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 55, 41))
        self.label_4.setStyleSheet("border-image: url(../image/matkhau.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 351, 331))
        self.label_2.setStyleSheet("border-image: url(../image/anhdangnhap.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 26))
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
        self.label.setText(_translate("MainWindow", "ĐĂNG NHẬP"))
        self.dang_nhap.setPlaceholderText(_translate("MainWindow", "Tên đăng nhập"))
        self.mat_khau.setPlaceholderText(_translate("MainWindow", "Mật khẩu"))
        self.btn_back.setText(_translate("MainWindow", "Thoát"))
        self.btn_login.setText(_translate("MainWindow", "Đăng nhập"))
        self.btn_login.clicked.connect(self.login)
        self.btn_back.clicked.connect(self.thoat_trang)
    def login(self):
        user = self.dang_nhap.text()
        pw = self.mat_khau.text()
        kn = ket_noi()
        sql = "SELECT vai_tro FROM nguoi_dung WHERE tai_khoan = %s AND mat_khau = %s"
        tham_so = (user, pw)
        try:
            nd = kn.lay_du_lieu(sql, tham_so)
            if nd:
                if nd[0] == ('ad',):
                    self.open_home_screen()
                elif nd[0] == ('nv',):
                    self.open_nv_screen()
            else:
                QMessageBox.warning(None, "Lỗi đăng nhập", "Thông tin đăng nhập không chính xác!")
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể kết nối cơ sở dữ liệu: {e}")

    def open_home_screen(self):
        try:
            subprocess.run(["python", "../home_admin/homea.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình quản trị: {e}")

    def open_nv_screen(self):
        try:
            subprocess.run(["python", "../home_nv/trang_chu.py"])
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể mở màn hình nhân viên: {e}")
    def thoat_trang(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
