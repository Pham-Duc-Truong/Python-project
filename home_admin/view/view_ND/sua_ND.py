from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class sua_nd(object):
    def __init__(self, gia_tri = []):
        self.gia_tri = gia_tri
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
        self.lb_tieu_de.setGeometry(QtCore.QRect(100, 8, 270, 55))
        self.lb_tieu_de.setObjectName("lb_tieu_de")
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")

        self.lb_id = QtWidgets.QLabel(parent=Form)
        self.lb_id.setGeometry(QtCore.QRect(40, 80, 100, 40))
        self.lb_id.setObjectName("lb_id")

        self.txt_id = QtWidgets.QTextEdit(parent=Form)
        self.txt_id.setGeometry(QtCore.QRect(170, 85, 200, 30))
        self.txt_id.setObjectName("txt_id")

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

        self.btn_sua = QtWidgets.QPushButton(parent=Form)
        self.btn_sua.setGeometry(QtCore.QRect(170, 300, 79, 37))
        self.btn_sua.setObjectName("btn_sua")
        self.btn_sua.setIcon(QtGui.QIcon("../image/edit.png"))
        self.btn_sua.setIconSize(QtCore.QSize(24, 24))
        self.btn_sua.clicked.connect(self.cap_nhat)

        self.nap_gia_tri()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def nap_gia_tri(self):
        if self.gia_tri:
            self.txt_id.setPlainText(self.gia_tri[0])
            self.txt_tai_khoan.setPlainText(self.gia_tri[1])
            self.txt_mat_khau.setPlainText(self.gia_tri[2])
            self.txt_vai_tro.setPlainText(self.gia_tri[3])

    def cap_nhat(self):
        try:
            kn = ket_noi()
            iD = self.txt_id.toPlainText()
            tk = self.txt_tai_khoan.toPlainText()
            mk = self.txt_mat_khau.toPlainText()
            vt = self.txt_vai_tro.toPlainText()

            kn.thuc_thi("UPDATE nguoi_dung SET tai_khoan = %s, mat_khau = %s, vai_tro = %s WHERE id = %s",
                        (tk, mk, vt, iD) )
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Sửa mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể sửa! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sửa người dùng"))
        self.lb_tieu_de.setText(_translate("Form", "Sửa người dùng"))
        self.lb_id.setText(_translate("Form", "ID"))
        self.lb_tai_khoan.setText(_translate("Form", "Tài khoản"))
        self.lb_mat_khau.setText(_translate("Form", "Mật khẩu"))
        self.lb_vai_tro.setText(_translate("Form", "Vai trò"))
        self.btn_sua.setText(_translate("Form", "Sửa"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = sua_nd()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

