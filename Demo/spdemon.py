class SanPham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia

    def get_ten(self):
        return self.__ten_san_pham
    def set_ten(self, ten_san_pham):
        self.__ten_san_pham = ten_san_pham

    def get_gia(self):
        return self.__gia
    def set_gia(self, gia):
        self.__gia = gia

    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia

    def thue_nhap_khau(self):
        return self.__gia * 0.1

    def nhap_thong_tin(self):
        self.__ten_san_pham = input("Tên sản phẩm: ")
        self.__gia = float(input("Giá: "))
        self.__giam_gia = float(input("Giảm giá: "))

    def xuat_tt_sp(self):
        print(f"Tên sản phẩm: {self.__ten_san_pham}")
        print(f"Giá: {self.__gia}")
        print(f"Giảm giá: {self.__giam_gia}")
        print(f"Thuế nhập khẩu: {self.thue_nhap_khau()}")

    def __str__(self):
        return f"Sản phẩm {self.__ten_san_pham} có giá {self.__gia} giảm giá {self.__giam_gia}"
