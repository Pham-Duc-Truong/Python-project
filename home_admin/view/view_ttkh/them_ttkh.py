from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class them_ttkh(object):
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
        self.lb_tieu_de.setGeometry(QtCore.QRect(0, 30, 390, 55))
        self.lb_tieu_de.setObjectName("lb_tieu_de")
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")

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

        self.btn_them = QtWidgets.QPushButton(parent=Form)
        self.btn_them.setGeometry(QtCore.QRect(150, 250, 100, 40))
        self.btn_them.setObjectName("btn_them")
        self.btn_them.setIcon(QtGui.QIcon("../image/add.png"))
        self.btn_them.setIconSize(QtCore.QSize(24, 24))
        self.btn_them.clicked.connect(self.them)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def them(self):
        try:
            kn = ket_noi()
            Ten = self.txt_ten.toPlainText()
            SDT = self.txt_sdt.toPlainText()
            kn.thuc_thi("INSERT INTO ttkh (ten, sdt) VALUES (%s, %s)", (Ten, SDT))
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Thêm mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể thêm mới! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Thêm thông tin khách hàng"))
        self.lb_tieu_de.setText(_translate("Form", "Thêm thông tin khách hàng"))
        self.lb_ten.setText(_translate("Form", "Tên"))
        self.lb_sdt.setText(_translate("Form", "SĐT"))
        self.btn_them.setText(_translate("Form", "Thêm"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = them_ttkh()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())