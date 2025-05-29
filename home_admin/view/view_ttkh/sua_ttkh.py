from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class sua_ttkh(object):
    def __init__(self, gia_tri = []):
        self.gia_tri = gia_tri

    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.resize(400, 320)
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
        self.lb_tieu_de.setGeometry(QtCore.QRect(0, 8, 390, 55))
        self.lb_tieu_de.setObjectName("lb_tieu_de")
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")

        self.lb_id = QtWidgets.QLabel(parent=Form)
        self.lb_id.setGeometry(QtCore.QRect(40, 80, 100, 40))
        self.lb_id.setObjectName("lb_id")

        self.txt_id = QtWidgets.QTextEdit(parent=Form)
        self.txt_id.setGeometry(QtCore.QRect(150, 85, 200, 30))
        self.txt_id.setObjectName("txt_id")

        self.lb_ten = QtWidgets.QLabel(parent=Form)
        self.lb_ten.setGeometry(QtCore.QRect(40, 130, 150, 48))
        self.lb_ten.setObjectName("lb_ten")

        self.txt_ten = QtWidgets.QTextEdit(parent=Form)
        self.txt_ten.setGeometry(QtCore.QRect(150, 140, 200, 30))
        self.txt_ten.setObjectName("txt_ten")

        self.lb_sdt = QtWidgets.QLabel(parent=Form)
        self.lb_sdt.setGeometry(QtCore.QRect(40, 190, 100, 40))
        self.lb_sdt.setObjectName("lb_sdt")

        self.txt_sdt = QtWidgets.QTextEdit(parent=Form)
        self.txt_sdt.setGeometry(QtCore.QRect(150, 195, 200, 30))
        self.txt_sdt.setObjectName("txt_sdt")

        self.btn_sua = QtWidgets.QPushButton(parent=Form)
        self.btn_sua.setGeometry(QtCore.QRect(150, 250, 80, 40))
        self.btn_sua.setObjectName("btn_sua")
        self.btn_sua.setIcon(QtGui.QIcon("../image/edit.png"))
        self.btn_sua.setIconSize(QtCore.QSize(24, 24))
        self.btn_sua.clicked.connect(self.cap_nhat)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.nap_gia_tri()

    def nap_gia_tri(self):
        if self.gia_tri:
            self.txt_id.setPlainText(self.gia_tri[0])
            self.txt_ten.setPlainText(self.gia_tri[1])
            self.txt_sdt.setPlainText(self.gia_tri[2])

    def cap_nhat(self):
        try:
            kn = ket_noi()
            iD = self.txt_id.toPlainText()
            ten = self.txt_ten.toPlainText()
            sdt = self.txt_sdt.toPlainText()
            kn.thuc_thi("UPDATE ttkh SET ten = %s, sdt = %s WHERE id = %s",
                        (ten, sdt, iD))
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Cập nhật thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể cập nhật! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sửa thông tin khách hàng"))
        self.lb_tieu_de.setText(_translate("Form", "Sửa thông tin khách hàng"))
        self.lb_id.setText(_translate("Form", "ID"))
        self.lb_ten.setText(_translate("Form", "Tên"))
        self.lb_sdt.setText(_translate("Form", "SĐT"))
        self.btn_sua.setText(_translate("Form", "Sửa"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = sua_ttkh()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())