from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class them_nd(object):
    def setupUi(self, Form):
        self.main = Form
        Form.setObjectName("Form")
        Form.resize(400, 400)
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
        self.lb_tieu_de.setGeometry(QtCore.QRect(100, 30, 270, 55))
        self.lb_tieu_de.setObjectName("lb_tieu_de")
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")

        self.lb_tai_khoan = QtWidgets.QLabel(parent=Form)
        self.lb_tai_khoan.setGeometry(QtCore.QRect(40, 130, 150, 48))
        self.lb_tai_khoan.setObjectName("lb_tai_khoan")

        self.txt_tai_khoan = QtWidgets.QTextEdit(parent=Form)
        self.txt_tai_khoan.setGeometry(QtCore.QRect(170, 140, 200, 30))
        self.txt_tai_khoan.setObjectName("txt_tai_khoan")

        self.lb_mat_khau = QtWidgets.QLabel(parent=Form)
        self.lb_mat_khau.setGeometry(QtCore.QRect(40, 190, 120, 40))
        self.lb_mat_khau.setObjectName("lb_mat_khau")

        self.txt_mat_khau = QtWidgets.QTextEdit(parent=Form)
        self.txt_mat_khau.setGeometry(QtCore.QRect(170, 195, 200, 30))
        self.txt_mat_khau.setObjectName("txt_mat_khau")

        self.lb_vai_tro = QtWidgets.QLabel(parent=Form)
        self.lb_vai_tro.setGeometry(QtCore.QRect(40, 250, 120, 40))
        self.lb_vai_tro.setObjectName("lb_vai_tro")

        self.txt_vai_tro = QtWidgets.QTextEdit(parent=Form)
        self.txt_vai_tro.setGeometry(QtCore.QRect(170, 255, 200, 30))
        self.txt_vai_tro.setObjectName("txt_vai_tro")

        self.btn_them = QtWidgets.QPushButton(parent=Form)
        self.btn_them.setGeometry(QtCore.QRect(170, 300, 79, 37))
        self.btn_them.setObjectName("btn_them")
        self.btn_them.setIcon(QtGui.QIcon("../image/add.png"))
        self.btn_them.setIconSize(QtCore.QSize(24, 24))
        self.btn_them.clicked.connect(self.them)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def them(self):
        try:
            kn = ket_noi()
            tk = self.txt_tai_khoan.toPlainText()
            mk = self.txt_mat_khau.toPlainText()
            vt = self.txt_vai_tro.toPlainText()
            kn.thuc_thi("INSERT INTO nguoi_dung (tai_khoan, mat_khau, vai_tro) VALUES (%s, %s, %s)",
                        (tk, mk, vt))
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Thêm mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể thêm mới! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Thêm người dùng"))
        self.lb_tieu_de.setText(_translate("Form", "Thêm người dùng"))
        self.lb_tai_khoan.setText(_translate("Form", "Tài khoản"))
        self.lb_mat_khau.setText(_translate("Form", "Mật khẩu"))
        self.lb_vai_tro.setText(_translate("Form", "Vai trò"))
        self.btn_them.setText(_translate("Form", "Thêm"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = them_nd()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

