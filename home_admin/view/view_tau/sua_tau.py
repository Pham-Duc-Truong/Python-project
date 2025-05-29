from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox
class sua_tau(object):
    def __init__(self, gia_tri = []):
        self.gia_tri = gia_tri
    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.resize(400, 320)
        Form.setStyleSheet("""
                QWidget {
                    background-color: #F5F5F5;
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
        self.lb_tieu_de.setGeometry(QtCore.QRect(130, 8, 270, 55))
        self.lb_tieu_de.setObjectName("lb_tieu_de")
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")

        self.lb_id = QtWidgets.QLabel(parent=Form)
        self.lb_id.setGeometry(QtCore.QRect(40, 80, 100, 40))
        self.lb_id.setObjectName("lb_id")

        self.txt_id = QtWidgets.QTextEdit(parent=Form)
        self.txt_id.setGeometry(QtCore.QRect(170, 85, 200, 30))
        self.txt_id.setObjectName("txt_id")

        self.lb_ten_tau = QtWidgets.QLabel(parent=Form)
        self.lb_ten_tau.setGeometry(QtCore.QRect(40, 130, 150, 48))
        self.lb_ten_tau.setObjectName("lb_ten_tau")

        self.txt_ten_tau = QtWidgets.QTextEdit(parent=Form)
        self.txt_ten_tau.setGeometry(QtCore.QRect(170, 140, 200, 30))
        self.txt_ten_tau.setObjectName("txt_ten_tau")

        self.lb_so_toa = QtWidgets.QLabel(parent=Form)
        self.lb_so_toa.setGeometry(QtCore.QRect(40, 190, 100, 40))
        self.lb_so_toa.setObjectName("lb_so_toa")

        self.txt_so_toa = QtWidgets.QTextEdit(parent=Form)
        self.txt_so_toa.setGeometry(QtCore.QRect(170, 195, 200, 30))
        self.txt_so_toa.setObjectName("txt_so_toa")

        self.btn_sua = QtWidgets.QPushButton(parent=Form)
        self.btn_sua.setGeometry(QtCore.QRect(150, 250, 100, 40))
        self.btn_sua.setObjectName("btn_them")
        self.btn_sua.setIcon(QtGui.QIcon("../image/edit.png"))
        self.btn_sua.setIconSize(QtCore.QSize(24, 24))
        self.btn_sua.clicked.connect(self.cap_nhat)
        self.nap_gia_tri()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def nap_gia_tri(self):
        if self.gia_tri:
            self.txt_id.setPlainText(self.gia_tri[0])
            self.txt_ten_tau.setPlainText(self.gia_tri[1])
            self.txt_so_toa.setPlainText(self.gia_tri[2])

    def cap_nhat(self):
        try:
            kn = ket_noi()
            Id = self.txt_id.toPlainText()
            ten = self.txt_ten_tau.toPlainText()
            sotoa = self.txt_so_toa.toPlainText()

            kn.thuc_thi("update tau set ten = %s, so_toa = %s where id = %s" , (ten, sotoa, Id))
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Sửa mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể Sửa! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sửa tàu"))
        self.lb_tieu_de.setText(_translate("Form", "Sửa tàu"))
        self.lb_id.setText(_translate("Form", "ID"))
        self.lb_ten_tau.setText(_translate("Form", "Tên tàu"))
        self.lb_so_toa.setText(_translate("Form", "Số toa"))
        self.btn_sua.setText(_translate("Form", "Sửa"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = sua_tau()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())