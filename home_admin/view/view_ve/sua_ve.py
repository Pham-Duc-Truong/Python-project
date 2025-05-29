from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class sua_ve(object):
    def __init__(self, gia_tri = []):
        self.gia_tri = gia_tri
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
                QPushButton:hover {
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

        self.lb_gia_tien = QtWidgets.QLabel(parent=Form)
        self.lb_gia_tien.setGeometry(QtCore.QRect(40, 130, 150, 48))
        self.lb_gia_tien.setObjectName("lb_gia_tien")

        self.txt_gia_tien = QtWidgets.QTextEdit(parent=Form)
        self.txt_gia_tien.setGeometry(QtCore.QRect(170, 140, 200, 30))
        self.txt_gia_tien.setObjectName("txt_gia_tien")

        self.lb_ten_toa = QtWidgets.QLabel(parent=Form)
        self.lb_ten_toa.setGeometry(QtCore.QRect(40, 190, 120, 40))
        self.lb_ten_toa.setObjectName("lb_ten_toa")

        self.txt_ten_toa = QtWidgets.QTextEdit(parent=Form)
        self.txt_ten_toa.setGeometry(QtCore.QRect(170, 195, 200, 30))
        self.txt_ten_toa.setObjectName("txt_ten_toa")

        self.lb_ten_tau = QtWidgets.QLabel(parent=Form)
        self.lb_ten_tau.setGeometry(QtCore.QRect(40, 250, 150, 40))
        self.lb_ten_tau.setObjectName("lb_ten_tau")

        self.combo_ten_tau = QtWidgets.QComboBox(parent=Form)
        self.combo_ten_tau.setGeometry(QtCore.QRect(170, 255, 200, 30))
        self.combo_ten_tau.setObjectName("txt_ten_tau")


        self.lb_id_ghe_ngoi = QtWidgets.QLabel(parent=Form)
        self.lb_id_ghe_ngoi.setGeometry(QtCore.QRect(40, 310, 120, 40))
        self.lb_id_ghe_ngoi.setObjectName("lb_id_ghe_ngoi")

        self.combo_ghe_ngoi = QtWidgets.QComboBox(parent=Form)
        self.combo_ghe_ngoi.setGeometry(QtCore.QRect(170, 315, 200, 30))
        self.combo_ghe_ngoi.setObjectName("txt_id_ghe_ngoi")


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
        du_lieu_ghengoi = kn.lay_du_lieu("SELECT id , tinh_trang FROM ghe_ngoi ")
        du_lieu_tau = kn.lay_du_lieu("SELECT id , ten FROM tau ")

        kn.ngat_ket_noi()
        for g1 in du_lieu_tau:
            text=str(g1[1])
            self.combo_ten_tau.addItem(text, g1[0])

        for g2 in du_lieu_ghengoi:
            text=str(g2[0])+'-'+str(g2[1])
            self.combo_ghe_ngoi.addItem(text, g2[0])

    def nap_gia_tri(self):
        if self.gia_tri:
            self.txt_id.setPlainText(self.gia_tri[0])
            self.txt_gia_tien.setPlainText(self.gia_tri[1])
            self.txt_ten_toa.setPlainText(self.gia_tri[2])

            id_index1 = self.combo_ten_tau.findText(self.gia_tri[3])
            self.combo_ten_tau.setCurrentIndex(id_index1)

            id_index2 = self.combo_ghe_ngoi.findData(self.gia_tri[5])
            self.combo_ghe_ngoi.setCurrentIndex(id_index2)


    def cap_nhat(self):
        try:
            kn = ket_noi()
            iD = self.txt_id.toPlainText()
            giatien = self.txt_gia_tien.toPlainText()
            tentoa = self.txt_ten_toa.toPlainText()
            tentau = self.combo_ten_tau.currentData()
            idghe_ngoi = self.combo_ghe_ngoi.currentData()
            print(iD)
            kn.thuc_thi("UPDATE ve_tau SET gia_tien = %s, ten_toa = %s, ten_tau = %s, id_ghe_ngoi = %s WHERE id = %s",
                        (giatien, tentoa, tentau, idghe_ngoi, iD) )
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Sửa mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể Sửa mới! Lỗi: {str(e)}")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sửa vé"))
        self.lb_tieu_de.setText(_translate("Form", "Sửa vé"))
        self.lb_id.setText(_translate("Form", "ID"))
        self.lb_gia_tien.setText(_translate("Form", "Giá tiền"))
        self.lb_ten_toa.setText(_translate("Form", "Tên toa"))
        self.lb_ten_tau.setText(_translate("Form", "Tên tàu"))
        self.lb_id_ghe_ngoi.setText(_translate("Form", "ID ghế ngồi"))

        self.btn_sua.setText(_translate("Form", "Sửa"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = sua_ve()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

