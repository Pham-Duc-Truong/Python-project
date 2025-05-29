from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class them_ve(object):
    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.resize(400, 490)
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

        self.lb_gia_tien = QtWidgets.QLabel(parent=Form)
        self.lb_gia_tien.setGeometry(QtCore.QRect(40, 130, 150, 48))
        self.lb_gia_tien.setObjectName("lb_gia_tien")

        self.txt_gia_tien = QtWidgets.QTextEdit(parent=Form)
        self.txt_gia_tien.setGeometry(QtCore.QRect(170, 140, 200, 30))
        self.txt_gia_tien.setObjectName("txt_gia_tien")

        self.lb_ten_toa = QtWidgets.QLabel(parent=Form)
        self.lb_ten_toa.setGeometry(QtCore.QRect(40, 190, 120, 40))
        self.lb_ten_toa.setObjectName("lb_ten_toa")

        self.combo_ten_toa = QtWidgets.QComboBox(parent=Form)
        self.combo_ten_toa.setGeometry(QtCore.QRect(170, 195, 200, 30))
        self.combo_ten_toa.setObjectName("txt_ten_toa")

        self.lb_ten_tau = QtWidgets.QLabel(parent=Form)
        self.lb_ten_tau.setGeometry(QtCore.QRect(40, 250, 150, 40))
        self.lb_ten_tau.setObjectName("lb_ten_tau")

        self.combo_ten_tau = QtWidgets.QComboBox(parent=Form)
        self.combo_ten_tau.setGeometry(QtCore.QRect(170, 255, 200, 30))
        self.combo_ten_tau.setObjectName("txt_ten_tau")

        self.lb_ghe_ngoi = QtWidgets.QLabel(parent=Form)
        self.lb_ghe_ngoi.setGeometry(QtCore.QRect(40, 310, 120, 40))
        self.lb_ghe_ngoi.setObjectName("lb_id_ghe_ngoi")

        self.combo_ghe_ngoi = QtWidgets.QComboBox(parent=Form)
        self.combo_ghe_ngoi.setGeometry(QtCore.QRect(170, 310, 200, 30))
        self.combo_ghe_ngoi.setObjectName("txt_id_ghe_ngoi")


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
        du_lieu_gn = kn.lay_du_lieu("SELECT id, tinh_trang FROM ghe_ngoi where tinh_trang = 'trống'")
        du_lieu_toa = kn.lay_du_lieu("SELECT id , ten FROM toa ")
        du_lieu_tau = kn.lay_du_lieu("SELECT id , ten FROM tau ")

        kn.ngat_ket_noi()
        for g1 in du_lieu_gn:
            text=str(g1[0])+" - "+str(g1[1])

            self.combo_ghe_ngoi.addItem(text, g1[0])

        for g2 in du_lieu_toa:
            text=str(g2[0])+" - "+str(g2[1])

            self.combo_ten_toa.addItem(text, g2[1])

        for g3 in du_lieu_tau:
            text=str(g3[0])+" - "+str(g3[1])

            self.combo_ten_tau.addItem(text, g3[1])

    def them(self):
        try:
            kn = ket_noi()
            giatien = self.txt_gia_tien.toPlainText()
            tentoa = self.combo_ten_toa.currentData()
            tentau = self.combo_ten_tau.currentData()
            idghe_ngoi = self.combo_ghe_ngoi.currentData()
            kn.thuc_thi("INSERT INTO ve_tau (gia_tien, ten_toa, ten_tau,id_ghe_ngoi) VALUES (%s, %s, %s, %s)", (giatien, tentoa, tentau,idghe_ngoi))
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Thêm mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể thêm mới! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Thêm vé"))
        self.lb_tieu_de.setText(_translate("Form", "Thêm vé"))
        self.lb_gia_tien.setText(_translate("Form", "Giá tiền"))
        self.lb_ten_toa.setText(_translate("Form", "Tên toa"))
        self.lb_ten_tau.setText(_translate("Form", "Tên tàu"))
        self.lb_ghe_ngoi.setText(_translate("Form", "Ghế ngồi"))


        self.btn_them.setText(_translate("Form", "Thêm"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = them_ve()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

