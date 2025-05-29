from ketnoi import ket_noi
class ChucNangDV:
    def lay_khach_theo_sdt(self,sdt=""):
        kn = ket_noi()
        data = kn.lay_du_lieu("select * from ttkh where sdt = %s",(sdt,))
        kn.ngat_ket_noi()
        if data:
            return [k[0] for k in data]
        else:
            return 0
    def dang_ki_ve(self,id_ve,id_khach):
        sql = "update ve_tau set id_kh = %s where id = %s and id_kh is null"
        kn = ket_noi()
        kn.thuc_thi(sql,(id_khach,id_ve))
        sql_lay_id_ghe = "select id_ghe_ngoi from ve_tau where id = %s"
        ghe = kn.lay_du_lieu(sql_lay_id_ghe,(id_ve,))
        if ghe:
            id_ghe = [g[0] for g in ghe]
            sql_update_ghe = "update ghe_ngoi set tinh_trang = %s where id = %s"
            kn.thuc_thi(sql_update_ghe,("không trống",id_ghe))
            sql_lay_id_toa = "select id_toa from ghe_ngoi where id = %s"
            toa = kn.lay_du_lieu(sql_lay_id_toa,(id_ghe,))
            if toa:
                id_toa = [t[0] for t in toa]
                sql_thuc_thi = "update toa set so_ghe_trong = so_ghe_trong - 1 where id = %s"
                kn.thuc_thi(sql_thuc_thi,id_toa)
        kn.ngat_ket_noi()