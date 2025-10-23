class SanPham:
    def __init__(self, ten_san_pham_t, gia_t, giam_gia_t):
        self.ten_san_pham = ten_san_pham_t
        self.gia = gia_t
        self.giam_gia = giam_gia_t



    def thue_nhap_khau(self):
        return self.gia * 0.1

    def nhap_thong_tin(self):
        self.ten_san_pham = input("Tên sản phẩm: ")
        self.gia = float(input("Giá: "))
        self.giam_gia = float(input("Giảm giá: "))

    def xuat_tt_sp(self):
        print(f"Tên sản phẩm: {self.ten_san_pham}")
        print(f"Giá: {self.gia}")
        print(f"Giảm giá: {self.giam_gia}")
        print(f"Thuế nhập khẩu: {self.thue_nhap_khau()}")

    def __str__(self):
        return f"Sản phẩm {self.ten_san_pham} có giá {self.gia} giảm giá {self.giam_gia}"
