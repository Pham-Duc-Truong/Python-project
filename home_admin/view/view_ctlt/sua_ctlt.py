
from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class sua_ctlt(object):
    def __init__(self, gia_tri = []):
        self.gia_tri = gia_tri
    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.resize(480, 270)
        Form.setStyleSheet("""

        QWidget {
            background-color: #EEEEEE;   
            color:black;      
        }
            QLabel {
            color: black;
            border-radius: 10px;
            padding: 8px;
            font-size: 20px;
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
                border-radius: 8px;

            }
            QPushButton#btn_sua:hover {
                background-color: #FFFF66;
            }

            QLabel#lb_tieu_de{
                font-size: 25px
            }

        """)
        self.lb_tieu_de = QtWidgets.QLabel(parent=Form)
        self.lb_tieu_de.setGeometry(QtCore.QRect(85, 20, 400, 50))
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")
        self.lb_tieu_de.setObjectName("lb_tieu_de")

        self.lb_id_tau = QtWidgets.QLabel(parent=Form)
        self.lb_id_tau.setGeometry(QtCore.QRect(90, 124, 80, 40))
        self.lb_id_tau.setStyleSheet("font-weight: bold;")
        self.lb_id_tau.setObjectName("lb_id_tau")

        self.combo_tau = QtWidgets.QComboBox(parent=Form)
        self.combo_tau.setGeometry(QtCore.QRect(180, 130, 211, 31))
        self.combo_tau.setObjectName("combo_id_tau")

        self.lb_lich = QtWidgets.QLabel(parent=Form)
        self.lb_lich.setGeometry(QtCore.QRect(90, 76, 80, 40))
        self.lb_lich.setStyleSheet("font-weight: bold;")
        self.lb_lich.setObjectName("lb_toa")

        self.combo_lich_trinh = QtWidgets.QComboBox(parent=Form)
        self.combo_lich_trinh.setGeometry(QtCore.QRect(180, 80, 211, 31))
        self.combo_lich_trinh.setObjectName("combo_id_lich")

        self.btn_sua = QtWidgets.QPushButton(parent=Form)
        self.btn_sua.setGeometry(QtCore.QRect(210, 200, 80, 35))
        self.btn_sua.setObjectName("btn_sua")
        self.btn_sua.setIcon(QtGui.QIcon("../image/edit.png"))
        self.btn_sua.setIconSize(QtCore.QSize(24, 24))
        self.btn_sua.clicked.connect(self.cap_nhat)

        self.nap_combo_tu_csdl()
        self.nap_gia_tri()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def nap_gia_tri(self):
        if self.gia_tri:
            id_index = self.combo_tau.findData(self.gia_tri[0])
            self.combo_tau.setCurrentIndex(id_index)

            id_index1 = self.combo_lich_trinh.findData(self.gia_tri[2])
            self.combo_lich_trinh.setCurrentIndex(id_index1)

    def nap_combo_tu_csdl(self):
        kn = ket_noi()
        du_lieu1 = kn.lay_du_lieu("SELECT id, ten FROM tau")
        du_lieu2 = kn.lay_du_lieu("SELECT * FROM lich_trinh")
        kn.ngat_ket_noi()

        for g1 in du_lieu2:
            text=str(g1[0])+" - "+str(g1[1])+" - "+str(g1[2])+" - "+str(g1[3])

            self.combo_lich_trinh.addItem(text, g1[0])

        for g2 in du_lieu1:
            text = str(g2[0]) + " - " + str(g2[1])
            self.combo_tau.addItem(text, g2[0])
    def cap_nhat(self):
        try:
            kn = ket_noi()
            idtau = self.combo_tau.currentData()
            idlich = self.combo_lich_trinh.currentData()
            print(idtau,idlich)
            kn.thuc_thi("UPDATE qlth.chi_tiet_lich_trinh set id_tau = %s WHERE id_lich = %s",
                        (idtau, idlich ))
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Sửa mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể sửa! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_tieu_de.setText(_translate("Form", "Sửa chi tiết lịch trình"))
        self.lb_id_tau.setText(_translate("Form", "Tàu"))
        self.lb_lich.setText(_translate("Form", "Lịch"))
        self.btn_sua.setText(_translate("Form", "Sửa"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = sua_ctlt()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
