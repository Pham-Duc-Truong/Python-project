from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class them_tau(object):
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
        self.lb_tieu_de.setGeometry(QtCore.QRect(130, 30, 270, 55))
        self.lb_tieu_de.setObjectName("lb_tieu_de")
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")

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

        self.btn_them = QtWidgets.QPushButton(parent=Form)
        self.btn_them.setGeometry(QtCore.QRect(170, 250, 100, 40))
        self.btn_them.setObjectName("btn_them")
        self.btn_them.setIcon(QtGui.QIcon("../image/add.png"))
        self.btn_them.setIconSize(QtCore.QSize(24, 24))
        self.btn_them.clicked.connect(self.them)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def them(self):
        try:
            kn = ket_noi()
            ten = self.txt_ten_tau.toPlainText()
            sotoa = self.txt_so_toa.toPlainText()

            kn.thuc_thi("INSERT INTO tau (ten, so_toa) VALUES (%s, %s)", (ten,sotoa))
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Thêm mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể thêm mới! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Thêm tàu"))
        self.lb_tieu_de.setText(_translate("Form", "Thêm tàu"))
        self.lb_ten_tau.setText(_translate("Form", "Tên tàu"))
        self.lb_so_toa.setText(_translate("Form", "Số toa"))
        self.btn_them.setText(_translate("Form", "Thêm"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = them_tau()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())