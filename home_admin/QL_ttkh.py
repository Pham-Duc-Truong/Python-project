from PyQt6 import QtCore, QtGui, QtWidgets
from chuc_nang import Chuc_nang
from view.view_ttkh.sua_ttkh import sua_ttkh
from view.view_ttkh.them_ttkh import them_ttkh
from ketnoi import ket_noi
from PyQt6.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(700, 550)
        Form.setStyleSheet("""
        QWidget {
            background-image: url("image.png"); /* Thêm ảnh */
            background-repeat: no-repeat;       /* Không lặp lại ảnh */
            background-position: center;        /* Canh giữa ảnh */
            background-color: #FFFFFF;         /* Màu nền đen */
            font-family: 'Segoe UI';           /* Font chữ */
        }

            QPushButton {
                background-color: #007AFF;  
                color: black;
                border: none;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                border: 2px solid #007AFF;
                border-radius: 8px;
            }
            QPushButton#pushButton:hover {
                background-color: #FFFF66;
            }

             QPushButton#pushButton_2:hover {
                background-color: #FFFF66;
            }

             QPushButton#pushButton_3:hover {
                background-color: #FFFF66;
            }

             QPushButton#pushButton_4:hover {
                background-color: #FFFF66;
            }

            QPushButton#pushButton {
                background-color: #FFFFFF; 

            }

            QPushButton#pushButton_2 {
                background-color: #FFFFFF; 
            }

            QPushButton#pushButton_3 {
                background-color: #FFFFFF; 
            }

            QPushButton#pushButton_4 {
                background-color: #FFFFFF; 
            }

            QTextEdit {
                border: 2px solid #007AFF;
                border-radius: 8px;
                padding: 5px;
                font-size: 14px;
                background-color: #FFFFFF;
                color:black;
            }
            QTableWidget {
                border: 2px solid #007AFF;
                border-radius: 5px;
                background-color: white;
                gridline-color: #007AFF;
                color: black;

            }
            QHeaderView::section {
                background-color: #FFCC33;
                color: black;
                font-size: 14px;
                padding: 5px;
                text-align: center;
                font-weight: bold;
            }
            QLabel {
                color: black;
                border: none;
                border-radius: 10px;
                padding: 8px;
                font-size: 20px;
            }
        """)

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(200, 10, 330, 50))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(160, 70, 200, 40))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 70, 100, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.tim_kiem)

        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 130, 620, 300))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Tên", "SĐT"])
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)

        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 460, 100, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QtGui.QIcon("../image/add.png"))
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.clicked.connect(self.them)

        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 460, 100, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon("../image/edit.png"))
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.clicked.connect(self.sua)

        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 460, 100, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setIcon(QtGui.QIcon("../image/delete.png"))
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.clicked.connect(self.xoa)

        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 460, 110, 40))
        self.pushButton_5.setObjectName("pushButton_4")
        self.pushButton_5.setIcon(QtGui.QIcon("../image/refresh.png"))
        self.pushButton_5.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_5.clicked.connect(self.nap_du_lieu)

        self.nap_du_lieu()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def nap_du_lieu(self):
        cn = Chuc_nang()
        cn.nap_du_lieu_vao_table(self.tableWidget, "select * from ttkh", None, ["ID", "Tên", "SĐT"])

    def them(self):
        self.Form = QtWidgets.QMainWindow()
        self.ui = them_ttkh()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def sua(self):
        dong = self.tableWidget.selectedItems()
        gia_tri = [d.text() for d in dong]
        if len(gia_tri) > 1:
            self.Form = QtWidgets.QMainWindow()
            self.ui = sua_ttkh(gia_tri)
            self.ui.setupUi(self.Form)
            self.Form.show()

    def xoa(self):
        dong = self.tableWidget.selectedItems()
        if not dong:  # Check if no row is selected
            QMessageBox.warning(None, "Cảnh báo", "Vui lòng chọn một dòng để xóa!")
            return
        gia_tri = [d.text() for d in dong]
        kn = ket_noi()
        sql = "DELETE FROM nguoi_dung WHERE id = %s"
        tham_so = (gia_tri[0],)
        try:
            kn.thuc_thi(sql, tham_so)
            QMessageBox.information(None, "Thành công", "Xóa thành công!")
        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Xóa không thành công! Lỗi: {str(e)}")

    def tim_kiem(self):
        cn = Chuc_nang()
        timkiem = self.textEdit.toPlainText().strip()

        if not timkiem:
            self.nap_du_lieu()
            return
        sql = """
            SELECT * FROM ttkh
            WHERE id LIKE %s OR ten LIKE %s OR sdt LIKE %s
        """
        tham_so = (f"%{timkiem}%", f"%{timkiem}%", f"%{timkiem}%")
        cn.nap_du_lieu_vao_table(self.tableWidget, sql, tham_so, ["ID", "Tên", "SĐT"])



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Quản lý thông tin khách hàng"))
        self.label.setText(_translate("Form", "Quản lý thông tin khách hàng"))
        self.pushButton.setText(_translate("Form", "🔍 Tìm kiếm"))
        self.pushButton_2.setText(_translate("Form", " Thêm"))
        self.pushButton_3.setText(_translate("Form", " Sửa"))
        self.pushButton_4.setText(_translate("Form", " Xóa"))
        self.pushButton_5.setText(_translate("Form", " Làm mới"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())