from ketnoi import ket_noi

class HDChucNang:
    def nap_ttkh(self,id,lb_ten,lb_sdt):
        kn = ket_noi()
        sql = "select ten,sdt from ttkh where id = %s"
        tham_so = (id,)
        dong = kn.lay_du_lieu(sql,tham_so)
        gia_tri_ten = [d[0] for d in dong]
        gia_tri_sdt = [d[1] for d in dong]
        kn.ngat_ket_noi()
        lb_ten.setText(gia_tri_ten[0])
        lb_sdt.setText(gia_tri_sdt[0])
    def nap_lich_trinh(self,id_ve,gio,don,den):
        sql = "select id_ghe_ngoi from ve_tau where id = %s"
        tham_so = (id_ve,)
        kn = ket_noi()
        ghe = kn.lay_du_lieu(sql,tham_so)
        if ghe:
            id_ghe = [g[0] for g in ghe]
            sql = "select id_toa from ghe_ngoi where id = %s"
            tham_so = (id_ghe,)
            toa = kn.lay_du_lieu(sql,tham_so)
            if toa:
                id_toa = [t[0] for t in toa]
                sql = "select id_tau from toa where id = %s"
                tham_so = (id_toa,)
                tau = kn.lay_du_lieu(sql,tham_so)
                if tau:
                    id_tau = [t[0] for t in tau]
                    sql = "select id_lich from chi_tiet_lich_trinh where id_tau = %s"
                    tham_so = (id_tau,)
                    ct = kn.lay_du_lieu(sql,tham_so)
                    if ct:
                        id_lich = [l[0] for l in ct]
                        sql = "select * from lich_trinh where id = %s"
                        tham_so = (id_lich[0],)
                        lt = kn.lay_du_lieu(sql,tham_so)
                        if lt:
                            text_gio = [l[1] for l in lt]
                            text_don = [l[2] for l in lt]
                            text_den = [l[3] for l in lt]
                            gio.setText(text_gio[0])
                            don.setText(text_don[0])
                            den.setText(text_den[0])
        kn.ngat_ket_noi()