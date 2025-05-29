from PyQt6.QtWidgets import QTableWidgetItem

from ketnoi import ket_noi
class ChucNang:

    def nap_du_lieu_vao_table(self,tb_ve,sql,tham_so=None):
        kn = ket_noi()
        data = kn.lay_du_lieu(sql,tham_so)
        self.nap_dong_vao_table(tb_ve,data)
        kn.ngat_ket_noi()
    def nap_dong_vao_table(self,tb_ve,data):
        if data:
            tb_ve.clear()
            tb_ve.setRowCount(len(data))
            tb_ve.setColumnCount(len(data[0]))
            tb_ve.setHorizontalHeaderLabels(["ID", "Giá tiền", "Tên toa", "Tên tàu", "Khách", "Ghế"])
            so_dong = 0
            for dong in data:
                so_cot = 0
                for cot in dong:
                    tb_ve.setItem(so_dong, so_cot, QTableWidgetItem(str(cot)))
                    so_cot += 1
                so_dong += 1
    def nap_du_lieu_vao_cbbox(self,cb_don,cb_den):
        kn = ket_noi()
        sql_don = "select diem_don from lich_trinh"
        data_don = kn.lay_du_lieu(sql_don)
        if data_don:
            for data in data_don:
                cb_don.addItem(data[0])
        sql_den = "select diem_den from lich_trinh"
        data_den = kn.lay_du_lieu(sql_den)
        if data_den:
            for data in data_den:
                cb_den.addItem(data[0])
        kn.ngat_ket_noi()
    def tim_kiem_ve(self,don,den,gio,tb_ve):
        list_tuple = ()
        kn = ket_noi()
        sql_lay_id_lt = "select id from lich_trinh where diem_don = %s and diem_den = %s and thoi_gian = %s"
        lt = kn.lay_du_lieu(sql_lay_id_lt,(don,den,gio))
        if lt:
            for l in lt:
                id_lt = l[0]
                sql_lay_id_tau = "select id_tau from chi_tiet_lich_trinh where id_lich = %s"
                tau = kn.lay_du_lieu(sql_lay_id_tau,(id_lt,))
                if tau:
                    for t in tau:
                        id_tau = t[0]
                        sql_lay_id_toa = "select id from toa where id_tau = %s"
                        toa = kn.lay_du_lieu(sql_lay_id_toa,(id_tau,))
                        if toa:
                            for t in toa:
                                id_toa = t[0]
                                sql_lay_id_ghe = "select id from ghe_ngoi where id_toa = %s and tinh_trang = %s"
                                ghe = kn.lay_du_lieu(sql_lay_id_ghe,(id_toa,"trống"))
                                if ghe:
                                    for g in ghe:
                                        id_ghe = g[0]
                                        sql_lay_ve = "select * from ve_tau where id_ghe_ngoi = %s"
                                        tham_so = (id_ghe,)
                                        ve = kn.lay_du_lieu(sql_lay_ve,tham_so)
                                        if ve:
                                            print(ve)
                                            list_tuple += ve
        self.nap_dong_vao_table(tb_ve, list_tuple)
        kn.ngat_ket_noi()

    def huy_ve(self,id):
        kn = ket_noi()
        sql = "update ve_tau set id_kh = NULL where id = %s"
        kn.thuc_thi(sql,(id,))
        sql_lay_ghe = "select id_ghe_ngoi from ve_tau where id = %s"
        ghe = kn.lay_du_lieu(sql_lay_ghe,(id,))
        id_ghe = [g[0] for g in ghe]
        sql_update_ghe = "update ghe_ngoi set tinh_trang = %s where id = %s"
        kn.thuc_thi(sql_update_ghe,("trống",id_ghe))
        sql_lay_toa = "select id_toa from ghe_ngoi where id = %s"
        toa = kn.lay_du_lieu(sql_lay_toa,(id_ghe,))
        id_toa = [t[0] for t in toa]
        sql_update_toa = "update toa set so_ghe_trong = so_ghe_trong + 1 where id = %s"
        kn.thuc_thi(sql_update_toa,id_toa)
        kn.ngat_ket_noi()