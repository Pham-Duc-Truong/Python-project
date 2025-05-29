from PyQt6.QtWidgets import QTableWidgetItem

from ketnoi import ket_noi

class Chuc_nang:

    def nap_du_lieu_vao_table(self, tb_ve, sql, tham_so=None, mang = []):
        kn = ket_noi()
        data = kn.lay_du_lieu(sql, tham_so)
        if data:
            tb_ve.setRowCount(len(data))
            tb_ve.setColumnCount(len(data[0]))
            tb_ve.setHorizontalHeaderLabels(mang)
            so_dong = 0
            for dong in data:
                so_cot = 0
                for cot in dong:
                    tb_ve.setItem(so_dong, so_cot, QTableWidgetItem(str(cot)))
                    so_cot += 1
                so_dong += 1
        kn.ngat_ket_noi()

    def cap_nhat (sql,tham_so= None):
        kn = ket_noi()
        kn.thuc_thi(sql,tham_so)
