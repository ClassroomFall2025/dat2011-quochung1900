class SinhVien:
    ten_sinh_vien = ""
    nam_sinh = ""
    truong = ""

    def __init__(self, tensv, namsinh, truonghoc):
        self.ten_sinh_vien = tensv
        self.nam_sinh = namsinh
        self.truong = truonghoc
    def doc_ten(self):
        return self.__ten_sinh_vien
    def ghi_ten(self, ten_moi):
        self.__ten_sinh_vien = ten_moi
    def xoa(self):
        pass
    def sua(self):
        pass
    def hien_thi_thong_tin(self):
        print(f"Sinh viên: {self.ten_sinh_vien} Sinh năm: {self.nam_sinh} Trường: {self.truong}")
    def __str__(self):
        return(f"Sinh viên {self.ten_sinh_vien} Sinh năm: {self.nam_sinh} trường: {self.truong}")

class SinhVienXLDL(SinhVien):

    def __init__(self, tensv, namsinh, truonghoc, laptrinh):
        SinhVien.__init__(self, tensv, namsinh, truonghoc, laptrinh)
        self.lap_trinh = laptrinh

    def __str__(self):
        return f"{SinhVien.__str__(str)}và học lập trình {self.lap_trinh}"

