from PyQt6 import QtCore, QtGui, QtWidgets
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox

class sua_gn(object):
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
        self.lb_tieu_de.setGeometry(QtCore.QRect(100, 8, 270, 55))
        self.lb_tieu_de.setObjectName("lb_tieu_de")
        self.lb_tieu_de.setStyleSheet("font-weight: bold;")

        self.lb_id = QtWidgets.QLabel(parent=Form)
        self.lb_id.setGeometry(QtCore.QRect(40, 80, 100, 40))
        self.lb_id.setObjectName("lb_id")

        self.txt_id = QtWidgets.QTextEdit(parent=Form)
        self.txt_id.setGeometry(QtCore.QRect(170, 85, 200, 30))
        self.txt_id.setObjectName("txt_id")

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

        self.btn_sua = QtWidgets.QPushButton(parent=Form)
        self.btn_sua.setGeometry(QtCore.QRect(150, 250, 80, 40))
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
        du_lieu1 = kn.lay_du_lieu("SELECT id, ten FROM toa")

        for g2 in du_lieu1:
            text = str(g2[0]) + " - " + str(g2[1])
            self.combo_toa.addItem(text, g2[0])

    def nap_gia_tri(self):
        if self.gia_tri:
            self.txt_id.setPlainText(self.gia_tri[0])
            self.txt_tinh_trang.setPlainText(self.gia_tri[1])
            id_index = self.combo_toa.findData(self.gia_tri[2])
            self.combo_toa.setCurrentIndex(id_index)


    def cap_nhat(self):
        try:
            kn = ket_noi()
            iD = self.txt_id.toPlainText()
            tinhtrang = self.txt_tinh_trang.toPlainText()
            idtoa = self.combo_toa.currentData()

            kn.thuc_thi("UPDATE ghe_ngoi SET tinh_trang = %s, id_toa = %s WHERE id = %s",
                        (tinhtrang,idtoa, iD) )
            kn.ngat_ket_noi()
            QMessageBox.information(None, "Thành công", "Sửa mới thành công!")
            self.main.close()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Không thể sửa! Lỗi: {str(e)}")



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sửa ghế ngồi"))
        self.lb_tieu_de.setText(_translate("Form", "Sửa ghế ngồi"))
        self.lb_id.setText(_translate("Form", "ID"))
        self.lb_tinh_trang.setText(_translate("Form", "Tình trạng"))
        self.lb_id_toa.setText(_translate("Form", "ID toa"))
        self.btn_sua.setText(_translate("Form", "Sửa"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = sua_gn()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())