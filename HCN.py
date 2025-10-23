class ChuNhat:
    def __int__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def nhap_thong_tin(self):
        self.dai = float(input("Nhập chiều dài: "))
        self.rong = float(input("Nhập chiều rộng: "))

    def tinh_chu_vi(self):
        return (self.dai + self.rong) *2
    
    def tinh_dien_tich(self):
        return self.dai * self.rong
    
    def xuat_thong_tin(self):
        print(f"Hình chữ nhật")
        print(f" Chiều dài: {self.dai}, Chiều rộng: {self.rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}, diện tích: {self.tinh_dien_tich()}")
    

class HinhVuong(ChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
    def nhap_thong_tin(self):
        self.canh= float(input("Nhập cạnh hình vuông: "))
    def tinh_dien_tich(self):
        return self.canh * self.canh
    def tinh_chu_vi(self):
        return self.canh * 4
    def xuat_thong_tin(self):
        print("Hình vuông")
        print(f"Cạnh: {self.canh}")
        print(f"Chu vi: {self.tinh_chu_vi()}, Diện tích: {self.tinh_dien_tich()}")

