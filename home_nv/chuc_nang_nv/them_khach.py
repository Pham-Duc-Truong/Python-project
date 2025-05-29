from ketnoi import ket_noi
class ChucNangTK:
    def them_khach(self,ten,sdt):
        kn = ket_noi()
        sql = "insert into ttkh (ten,sdt) values(%s,%s)"
        kn.thuc_thi(sql,(ten,sdt))
        kn.ngat_ket_noi()