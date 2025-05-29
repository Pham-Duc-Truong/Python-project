from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from tkinter import messagebox
from PyQt6.QtWidgets import QMessageBox

class sua_toa(object):
    def __init__(self, gia_tri = []):
        self.gia_tri = gia_tri
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
                QPushButton#btn_sua:hover {
                    background-color: #FFFF66;
                }

                QLabel#lb_tieu_de {
                    font-size: 28px;
                    text-align: center;
                }
        """)

        self.lb_tieu_de = QtWidgets.QLabel(parent=Form)
        self.lb_tieu_de.setGeometry(QtCore.QRect(130, 8, 270, 55))
        self.lb_tieu_de.setObjectName("lb_tieu_de")
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")

        self.lb_id = QtWidgets.QLabel(parent=Form)
        self.lb_id.setGeometry(QtCore.QRect(40, 80, 100, 40))
        self.lb_id.setObjectName("lb_id")

        self.txt_id = QtWidgets.QTextEdit(parent=Form)
        self.txt_id.setGeometry(QtCore.QRect(170, 85, 200, 30))
        self.txt_id.setObjectName("txt_id")

        self.lb_ten_toa = QtWidgets.QLabel(parent=Form)
        self.lb_ten_toa.setGeometry(QtCore.QRect(40, 130, 150, 48))
        self.lb_ten_toa.setObjectName("lb_ten_toa")

        self.combo_toa = QtWidgets.QComboBox(parent=Form)
        self.combo_toa.setGeometry(QtCore.QRect(170, 140, 200, 30))
        self.combo_toa.setObjectName("txt_ten_toa")

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


        self.btn_sua = QtWidgets.QPushButton(parent=Form)
        self.btn_sua.setGeometry(QtCore.QRect(170, 370, 79, 37))
        self.btn_sua.setObjectName("btn_sua")
        self.btn_sua.setIcon(QtGui.QIcon("../image/edit.png"))
        self.btn_sua.setIconSize(QtCore.QSize(24, 24))
        self.btn_sua.clicked.connect(self.cap_nhat)


        self.nap_combo_tu_csdl()
        self.nap_gia_tri()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def nap_combo_tu_csdl(self):
        kn = ket_noi()
        du_lieu_toa = kn.lay_du_lieu("SELECT id , ten FROM toa ")
        du_lieu_tau = kn.lay_du_lieu("SELECT id , ten FROM tau ")


        kn.ngat_ket_noi()
        for g1 in du_lieu_tau:
            text=str(g1[1])

            self.combo_tau.addItem(text, g1[0])

        for g2 in du_lieu_toa:
            text=str(g2[1])

            self.combo_toa.addItem(text, g2[0])

    def nap_gia_tri(self):
        if self.gia_tri:
            self.txt_id.setPlainText(self.gia_tri[0])

            id_index1 = self.combo_toa.findText(self.gia_tri[1])
            self.combo_toa.setCurrentIndex(id_index1)

            self.txt_tong_ghe.setPlainText(self.gia_tri[2])
            self.txt_so_ghe_trong.setPlainText(self.gia_tri[3])
            id_index = self.combo_tau.findData(self.gia_tri[4])
            self.combo_tau.setCurrentIndex(id_index)

    def kiem_tra_ghe_trong(self, ghe_trong, ghe):
        if ghe_trong <= ghe:
            return True
        return False

    def cap_nhat(self):
        try:
            kn = ket_noi()
            iD = self.txt_id.toPlainText()
            ten = self.combo_toa.currentData()
            tongghe = self.txt_tong_ghe.toPlainText()
            soghetrong = self.txt_so_ghe_trong.toPlainText()
            idtau = self.combo_tau.currentData()
            if self.kiem_tra_ghe_trong(soghetrong, tongghe):
                kn.thuc_thi("UPDATE toa SET ten = %s, tong_ghe = %s, so_ghe_trong = %s, id_tau = %s WHERE id = %s",
                            (ten, tongghe, soghetrong, idtau, iD))
                kn.ngat_ket_noi()
                QMessageBox.information(None, "Thành công", "Cập nhật thành công!")
                self.main.close()
            else:
                QMessageBox.warning(None, "Cảnh báo", "Vui lòng nhập số ghế trống nhỏ hơn tổng ghế!")
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Cập nhật không thành công! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sửa toa"))
        self.lb_tieu_de.setText(_translate("Form", "Sửa toa"))
        self.lb_id.setText(_translate("Form", "ID"))
        self.lb_ten_toa.setText(_translate("Form", "Tên toa"))
        self.lb_tong_ghe.setText(_translate("Form", "Tổng ghế"))
        self.lb_so_ghe_trong.setText(_translate("Form", "Số ghế trống"))
        self.lb_id_tau.setText(_translate("Form", "ID tàu"))
        self.btn_sua.setText(_translate("Form", "Sửa"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = sua_toa()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

