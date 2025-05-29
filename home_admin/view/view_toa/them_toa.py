from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi

class them_toa(object):
    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.resize(400, 430)
        Form.setStyleSheet("""
                QWidget {
                    background-color: #F5F5F5;
                    color:black;
                }
                QLabel {
                color: black;
                border-radius: 10px;
                padding: 8px;
                font-size: 18px;
                font-weight: bold;
                }
                QTextEdit {
                    border: 2px solid #007AFF;
                    border-radius: 8px;
                    padding: 5px;
                    font-size: 14px;
                    background-color: #FFFFFF;
                    color:black;
                }
                QComboBox {
                border: 2px solid #007AFF;
                border-radius: 8px;
                padding: 5px;
                font-size: 14px;
                background-color: #FFFFFF;
                color:black;
                }                    
                QComboBox QAbstractItemView {
                     background-color: #FFFFFF; /* Đặt nền màu trắng cho danh sách thả xuống */
                }
                QPushButton {
                background-color: #FFFFFF;  
                color: black;
                border: none;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                border: 2px solid #007AFF;
                border-radius: 8px;;
                }
                QPushButton#btn_them:hover {
                    background-color: #FFFF66;
                }

                QLabel#lb_tieu_de {
                    font-size: 28px;
                    text-align: center;
                }
        """)

        self.lb_tieu_de = QtWidgets.QLabel(parent=Form)
        self.lb_tieu_de.setGeometry(QtCore.QRect(130, 30, 270, 55))
        self.lb_tieu_de.setObjectName("lb_tieu_de")
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")

        self.lb_ten_toa = QtWidgets.QLabel(parent=Form)
        self.lb_ten_toa.setGeometry(QtCore.QRect(40, 130, 150, 48))
        self.lb_ten_toa.setObjectName("lb_ten_toa")

        self.txt_ten_toa = QtWidgets.QTextEdit(parent=Form)
        self.txt_ten_toa.setGeometry(QtCore.QRect(170, 140, 200, 30))
        self.txt_ten_toa.setObjectName("txt_ten_toa")

        self.lb_tong_ghe = QtWidgets.QLabel(parent=Form)
        self.lb_tong_ghe.setGeometry(QtCore.QRect(40, 190, 120, 40))
        self.lb_tong_ghe.setObjectName("lb_tong_ghe")

        self.txt_tong_ghe = QtWidgets.QTextEdit(parent=Form)
        self.txt_tong_ghe.setGeometry(QtCore.QRect(170, 195, 200, 30))
        self.txt_tong_ghe.setObjectName("txt_tong_ghe")

        self.lb_so_ghe_trong = QtWidgets.QLabel(parent=Form)
        self.lb_so_ghe_trong.setGeometry(QtCore.QRect(40, 250, 150, 40))
        self.lb_so_ghe_trong.setObjectName("lb_so_ghe_trong")

        self.txt_so_ghe_trong = QtWidgets.QTextEdit(parent=Form)
        self.txt_so_ghe_trong.setGeometry(QtCore.QRect(170, 255, 200, 30))
        self.txt_so_ghe_trong.setObjectName("txt_so_ghe_trong")

        self.lb_id_tau = QtWidgets.QLabel(parent=Form)
        self.lb_id_tau.setGeometry(QtCore.QRect(40, 310, 120, 40))
        self.lb_id_tau.setObjectName("lb_id_tau")

        self.combo_tau = QtWidgets.QComboBox(parent=Form)
        self.combo_tau.setGeometry(QtCore.QRect(170, 315, 200, 30))
        self.combo_tau.setObjectName("txt_id_tau")


        self.btn_them = QtWidgets.QPushButton(parent=Form)
        self.btn_them.setGeometry(QtCore.QRect(170, 370, 79, 37))
        self.btn_them.setObjectName("btn_them")
        self.btn_them.setIcon(QtGui.QIcon("../image/add.png"))
        self.btn_them.setIconSize(QtCore.QSize(24, 24))
        self.btn_them.clicked.connect(self.them)

        self.nap_combo_tu_csdl()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def nap_combo_tu_csdl(self):
        kn = ket_noi()
        du_lieu_tau = kn.lay_du_lieu("SELECT id , ten FROM tau ")

        kn.ngat_ket_noi()
        for g1 in du_lieu_tau:
            text=str(g1[0])+" - "+str(g1[1])

            self.combo_tau.addItem(text, g1[0])

    def kiem_tra_ghe_trong(self, ghe_trong, ghe):
        if ghe_trong <= ghe:
            return True
        return False

    def them(self):
        kn = ket_noi()
        ten = self.txt_ten_toa.toPlainText()
        tongghe = self.txt_tong_ghe.toPlainText()
        soghetrong = self.txt_so_ghe_trong.toPlainText()
        idtau = self.combo_tau.currentData()
        if self.kiem_tra_ghe_trong(soghetrong, tongghe):
            kn.thuc_thi("INSERT INTO toa (ten, tong_ghe, so_ghe_trong, id_tau) VALUES (%s, %s, %s, %s)",
                        (ten, tongghe, soghetrong, idtau))
            kn.ngat_ket_noi()
            self.main.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Thêm toa"))
        self.lb_tieu_de.setText(_translate("Form", "Thêm toa"))
        self.lb_ten_toa.setText(_translate("Form", "Tên toa"))
        self.lb_tong_ghe.setText(_translate("Form", "Tổng ghế"))
        self.lb_so_ghe_trong.setText(_translate("Form", "Số ghế trống"))
        self.lb_id_tau.setText(_translate("Form", "ID tàu"))

        self.btn_them.setText(_translate("Form", "Thêm"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = them_toa()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

