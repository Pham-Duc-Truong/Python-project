from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi

class them_lich_trinh(object):
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

        self.lb_thoi_gian = QtWidgets.QLabel(parent=Form)
        self.lb_thoi_gian.setGeometry(QtCore.QRect(40, 130, 150, 48))
        self.lb_thoi_gian.setObjectName("lb_thoi_gian")

        self.txt_thoi_gian = QtWidgets.QTextEdit(parent=Form)
        self.txt_thoi_gian.setGeometry(QtCore.QRect(170, 140, 200, 30))
        self.txt_thoi_gian.setObjectName("txt_thoi_gian")

        self.lb_diem_don = QtWidgets.QLabel(parent=Form)
        self.lb_diem_don.setGeometry(QtCore.QRect(40, 190, 120, 40))
        self.lb_diem_don.setObjectName("lb_diem_don")

        self.txt_diem_don = QtWidgets.QTextEdit(parent=Form)
        self.txt_diem_don.setGeometry(QtCore.QRect(170, 195, 200, 30))
        self.txt_diem_don.setObjectName("txt_diem_don")

        self.lb_diem_den = QtWidgets.QLabel(parent=Form)
        self.lb_diem_den.setGeometry(QtCore.QRect(40, 250, 120, 40))
        self.lb_diem_den.setObjectName("lb_diem_den")

        self.txt_diem_den = QtWidgets.QTextEdit(parent=Form)
        self.txt_diem_den.setGeometry(QtCore.QRect(170, 255, 200, 30))
        self.txt_diem_den.setObjectName("txt_diem_den")

        self.btn_them = QtWidgets.QPushButton(parent=Form)
        self.btn_them.setGeometry(QtCore.QRect(170, 300, 79, 37))
        self.btn_them.setObjectName("btn_them")
        self.btn_them.setIcon(QtGui.QIcon("../image/add.png"))
        self.btn_them.setIconSize(QtCore.QSize(24, 24))
        self.btn_them.clicked.connect(self.them)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def them(self):
        kn = ket_noi()
        tg = self.txt_thoi_gian.toPlainText()
        ddon = self.txt_diem_don.toPlainText()
        dden = self.txt_diem_den.toPlainText()
        kn.thuc_thi("INSERT INTO lich_trinh (thoi_gian, diem_don, diem_den) VALUES (%s, %s, %s)",
                    (tg, ddon, dden))
        kn.ngat_ket_noi()
        self.main.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Thêm lịch trình"))
        self.lb_tieu_de.setText(_translate("Form", "Thêm lịch trình"))
        self.lb_thoi_gian.setText(_translate("Form", "Thời gian"))
        self.lb_diem_don.setText(_translate("Form", "Điểm đón"))
        self.lb_diem_den.setText(_translate("Form", "Điểm đến"))
        self.btn_them.setText(_translate("Form", "Thêm"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = them_lich_trinh()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())