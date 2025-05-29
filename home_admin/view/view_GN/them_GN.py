from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class them_gn(object):
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

        self.lb_tinh_trang = QtWidgets.QLabel(parent=Form)
        self.lb_tinh_trang.setGeometry(QtCore.QRect(40, 130, 150, 48))
        self.lb_tinh_trang.setObjectName("lb_tinh_trang")

        self.txt_tinh_trang = QtWidgets.QTextEdit(parent=Form)
        self.txt_tinh_trang.setGeometry(QtCore.QRect(170, 140, 200, 30))
        self.txt_tinh_trang.setObjectName("txt_tinh_trang")

        self.lb_id_toa = QtWidgets.QLabel(parent=Form)
        self.lb_id_toa.setGeometry(QtCore.QRect(40, 190, 100, 40))
        self.lb_id_toa.setObjectName("lb_id_toa")

        self.combo_toa = QtWidgets.QComboBox(parent=Form)
        self.combo_toa.setGeometry(QtCore.QRect(170, 195, 200, 30))
        self.combo_toa.setObjectName("txt_id_toa")

        self.btn_them = QtWidgets.QPushButton(parent=Form)
        self.btn_them.setGeometry(QtCore.QRect(170, 250, 80, 40))
        self.btn_them.setObjectName("btn_them")
        self.btn_them.setIcon(QtGui.QIcon("../image/add.png"))
        self.btn_them.setIconSize(QtCore.QSize(24, 24))
        self.btn_them.clicked.connect(self.them)

        self.nap_combo_tu_csdl()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def nap_combo_tu_csdl(self):
        kn = ket_noi()
        du_lieu1 = kn.lay_du_lieu("SELECT id, ten FROM toa")

        for g2 in du_lieu1:
            text = str(g2[0]) + " - " + str(g2[1])
            self.combo_toa.addItem(text, g2[0])

    def them(self):
        try:
            kn = ket_noi()
            tinhtrang = self.txt_tinh_trang.toPlainText()
            idtoa = self.combo_toa.currentData()
            kn.thuc_thi("INSERT INTO ghe_ngoi (tinh_trang, id_toa) VALUES (%s, %s)", (tinhtrang, idtoa))
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Thêm mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể thêm mới! Lỗi: {str(e)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Thêm ghế ngồi"))
        self.lb_tieu_de.setText(_translate("Form", "Thêm ghế ngồi"))
        self.lb_tinh_trang.setText(_translate("Form", "Tình trạng"))
        self.lb_id_toa.setText(_translate("Form", "Toa"))
        self.btn_them.setText(_translate("Form", "Thêm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = them_gn()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())