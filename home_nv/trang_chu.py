
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

from home_nv.chuc_nang_nv.trang_chu import ChucNang
from  home_nv.dat_ve import Ui_DVWindow
from home_nv.hoa_don import Ui_HDWindow
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_dat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_dat.setGeometry(QtCore.QRect(250, 490, 121, 41))
        self.btn_dat.setStyleSheet("background-color : rgb(29, 255, 55);font-weight : bold;text-align:center")
        self.btn_dat.setObjectName("btn_dat")
        self.btn_huy = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_huy.setGeometry(QtCore.QRect(80, 490, 121, 41))
        self.btn_huy.setStyleSheet("background-color :rgb(170, 11, 22);font-weight:bold;")
        self.btn_huy.setObjectName("btn_huy")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("font-size:18px")
        self.label.setGeometry(QtCore.QRect(310, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tb_ve = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tb_ve.setGeometry(QtCore.QRect(100, 160, 591, 291))
        self.tb_ve.setObjectName("tb_ve")
        self.tb_ve.setColumnCount(0)
        self.tb_ve.setRowCount(0)
        self.cb_don = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cb_don.setGeometry(QtCore.QRect(230, 70, 101, 31))
        self.cb_don.setObjectName("cb_don")
        self.btn_tim = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_tim.setGeometry(QtCore.QRect(510, 100, 121, 41))
        self.btn_tim.setStyleSheet("background-color : rgb(8, 119, 255);\n"
"font-weight : bold;")
        self.btn_tim.setObjectName("btn_tim")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 120, 49, 16))
        self.label_2.setObjectName("label_2")
        self.cb_den = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cb_den.setGeometry(QtCore.QRect(230, 110, 101, 31))
        self.cb_den.setObjectName("cb_den")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 80, 51, 16))
        self.label_3.setObjectName("label_3")
        self.btn_lam_moi = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_lam_moi.setGeometry(QtCore.QRect(420, 490, 121, 41))
        self.btn_lam_moi.setStyleSheet("background-color : rgb(202, 101, 0);\n"
"font-weight : bold")
        self.btn_lam_moi.setObjectName("btn_lam_moi")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 120, 49, 16))
        self.label_4.setObjectName("label_4")
        self.cb_gio = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cb_gio.setGeometry(QtCore.QRect(400, 110, 101, 31))
        self.cb_gio.setObjectName("cb_gio")
        self.btn_in = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_in.setGeometry(QtCore.QRect(590, 490, 121, 41))
        self.btn_in.setStyleSheet("background-color : rgb(2, 99, 255);\n"
"font-weight : bold")
        self.btn_in.setObjectName("btn_in")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.nap_data()
        self.btn_lam_moi.clicked.connect(self.nap_data)
        self.btn_tim.clicked.connect(self.tim_kiem)
        self.btn_tim.setIcon(QIcon("../image/find.png"))
        self.btn_tim.setIconSize(QSize(25,25))
        self.btn_dat.clicked.connect(self.dat_ve)
        self.btn_dat.setIcon(QIcon("../image/add.png"))
        self.btn_dat.setIconSize(QSize(25,25))
        self.btn_huy.setIcon(QIcon("../image/delete.png"))
        self.btn_huy.setIconSize(QSize(25,25))
        self.btn_huy.clicked.connect(self.huy)
        self.btn_lam_moi.setIcon(QIcon("../image/refresh.png"))
        self.btn_lam_moi.setIconSize(QSize(25,25))
        self.btn_in.clicked.connect(self.in_hoa_don)
        self.btn_in.setIcon(QIcon("../image/edit.png"))
        self.btn_in.setIconSize(QSize(25,25))
        self.cb_gio.addItem("6h")
        self.cb_gio.addItem("12h")
        self.cb_gio.addItem("18h")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_dat.setText(_translate("MainWindow", "Đặt vé"))
        self.btn_huy.setText(_translate("MainWindow", "Hủy vé"))
        self.label.setText(_translate("MainWindow", "Đặt vé tàu hỏa cho khách"))
        self.btn_tim.setText(_translate("MainWindow", "Tìm kiếm"))
        self.label_2.setText(_translate("MainWindow", "điểm đến"))
        self.label_3.setText(_translate("MainWindow", "điểm đón"))
        self.btn_lam_moi.setText(_translate("MainWindow", "Làm mới"))
        self.label_4.setText(_translate("MainWindow", "thời gian"))
        self.btn_in.setText(_translate("MainWindow", "In hóa đơn"))
    def nap_data(self):
        self.cb_don.clear()
        self.cb_den.clear()
        cn = ChucNang()
        sql = "select * from ve_tau"
        cn.nap_du_lieu_vao_table(self.tb_ve,sql)
        cn.nap_du_lieu_vao_cbbox(self.cb_don,self.cb_den)
    def tim_kiem(self):
        cn = ChucNang()
        cn.tim_kiem_ve(self.cb_don.currentText(),self.cb_den.currentText(),self.cb_gio.currentText(),self.tb_ve)
    def dat_ve(self):
        dong = self.tb_ve.selectedItems()
        gia_tri = [d.text() for d in dong]
        self.mo_dat_ve(gia_tri)
    def mo_dat_ve(self,gia_tri=None):
        self.window = QtWidgets.QMainWindow()  # Hoặc QWidget()
        self.dv = Ui_DVWindow(gia_tri)  # Khởi tạo giao diện
        self.dv.setupUi(self.window)  # Gán giao diện vào cửa sổ
        self.window.show()
    def huy(self):
        dong = self.tb_ve.selectedItems()
        gia_tri = [d.text() for d in dong]
        cn = ChucNang()
        if len(gia_tri) > 1:
            cn.huy_ve(gia_tri[0])
            self.nap_data()
    def in_hoa_don(self):
        dong = self.tb_ve.selectedItems()
        if len(dong) > 1:
            gia_tri = [d.text() for d in dong]

            self.HDWindow = QtWidgets.QMainWindow()
            self.ui_hd = Ui_HDWindow(gia_tri)
            self.ui_hd.setupUi(self.HDWindow)
            self.HDWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
