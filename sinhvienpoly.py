class SinhVienPoly:
    def __init__(self, ten_sinh_vien , nganh_hoc):
        self.ten_sinh_vien = ten_sinh_vien
        self.nganh_hoc = nganh_hoc
        
    def nhap_thong_tin(self):
        pass 

    def get_diem(self):
        return 0.0 
        
    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem >= 9 and diem <=10:
            return "xuất sắc"
        elif diem >= 8:
            return "Giỏi"
        elif diem >= 7:
            return "Khá"
        elif diem >=5:
            return "Trung bình"
        else:
            return "Chưa đạt"
    def xuat_thong_tin(self):
        print(f"Tên SV: {self.ten_sinh_vien:<20} | Ngành: {self.nganh_hoc:<10} | Điểm: {self.get_diem():<10.2f} | Học lực: {self.get_hoc_luc()}")
    
class sinhvienIT(SinhVienPoly):
    def __init__(self, ten_sinh_vien, nganh_hoc, java, html, css):
        super().__init__(ten_sinh_vien, nganh_hoc)
        self.java = java
        self.html = html
        self.css = css
    def get_diem(self):
        return float((self.java*2 + self.html + self.css)/4)
    
class SinhVieniz(SinhVienPoly):
    def __init__(self, ten_sinh_vien, nganh_hoc, marketing, sales):
        super().__init__(ten_sinh_vien, nganh_hoc)
        self.marketing = marketing
        self.sales = sales
    def get_diem(self):
        return float((self.marketing + self.sales)/2)

danh_sach_sinh_vien = []

def nhap_danh_sach():
    print("--- Nhập sinh viên ---")
    loai_sv = input("Bạn muốn nhập sinh viên IT hay Iz? (IT/Iz): ").upper()
    if loai_sv == "IT":
        ten = input("Nhập tên sinh viên: ")
        nganh = "IT"
        java = float(input("Nhập điểm Java: "))
        html = float(input("Nhập điểm HTML: "))
        css = float(input("Nhập điểm CSS: "))
        sv_moi = sinhvienIT(ten, nganh, java, html, css)
        danh_sach_sinh_vien.append(sv_moi)
        print("Đã thêm sinh viên IT thành công!")
    elif loai_sv == "IZ":
        ten = input("Nhập tên sinh viên: ")
        nganh = "Iz"
        marketing = float(input("Nhập điểm Marketing: "))
        sales = float(input("Nhập điểm Sales: "))
        sv_moi = SinhVieniz(ten, nganh, marketing, sales)
        danh_sach_sinh_vien.append(sv_moi)
        print("Đã thêm sinh viên Iz thành công!")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

def xuat_danh_sach():
    if not danh_sach_sinh_vien:
        print("Danh sách sinh viên trống.")
        return
    print("\n--- Danh sách sinh viên ---")
    print(f"{'Tên sinh viên':<20} {'Ngành':<10} {'Điểm':<10} {'Học lực':<10}")
    print("="*60)
    for sv in danh_sach_sinh_vien:
        sv.xuat_thong_tin()
    print("="*60)

def xuat_hoc_luc_gioi():
    if not danh_sach_sinh_vien:
        print("Danh sách sinh viên trống.")
        return
    
    found = False
    print("\n--- Danh sách sinh viên có học lực Giỏi và Xuất sắc ---")
    print(f"{'Tên sinh viên':<20} {'Ngành':<10} {'Điểm':<10} {'Học lực':<10}")
    print("="*60)
    for sv in danh_sach_sinh_vien:
        hoc_luc = sv.get_hoc_luc()
        if hoc_luc in ["Giỏi", "xuất sắc"]:
            sv.xuat_thong_tin()
            found = True
    if not found:
        print("Không có sinh viên nào có học lực Giỏi hoặc Xuất sắc.")
    print("="*60)

def sap_xep_diem():
    if not danh_sach_sinh_vien:
        print("Danh sách sinh viên trống.")
        return
    
    
    danh_sach_sinh_vien.sort(key=lambda sv: sv.get_diem())
    print("Đã sắp xếp danh sách sinh viên theo điểm.")
    xuat_danh_sach()


while True:
    print("\n========== MENU QUẢN LÝ SINH VIÊN ==========")
    print("1. Nhập danh sách sinh viên")
    print("2. Xuất thông tin danh sách sinh viên")
    print("3. Xuất danh sách sinh viên có học lực giỏi")
    print("4. Sắp xếp danh sách sinh viên theo điểm")
    print("5. Kết thúc")
    print("============================================")
    
    try:
        chon = int(input("Nhập lựa chọn của bạn (1-5): "))
        if chon == 1:
            nhap_danh_sach()
        elif chon == 2:
            xuat_danh_sach()
        elif chon == 3:
            xuat_hoc_luc_gioi()
        elif chon == 4:
            sap_xep_diem()
        elif chon == 5:
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")
    except ValueError:
        print("Lựa chọn không hợp lệ. Vui lòng nhập một số.")