def nhap_danh_sach():
    print("[Y1] Nhập danh sách nhân viên và lưu vào file.")

def doc_tu_file():
    print("[Y2] Đọc danh sách nhân viên từ file và hiển thị.")

def tim_theo_ma():
    print("[Y3] Tìm và hiển thị nhân viên theo mã.")

def xoa_theo_ma():
    print("[Y4] Xóa nhân viên theo mã và cập nhật file.")

def cap_nhat_nhan_vien():
    print("[Y5] Cập nhật thông tin nhân viên và ghi vào file.")

def tim_theo_luong():
    print("[Y6] Tìm nhân viên theo khoảng lương.")

def sap_xep_ten():
    print("[Y7] Sắp xếp danh sách theo họ và tên.")

def sap_xep_thu_nhap():
    print("[Y8] Sắp xếp danh sách theo thu nhập.")

def top_5_thu_nhap():
    print("[Y9] Hiển thị 5 nhân viên có thu nhập cao nhất.")

def menu_quan_ly_nhan_vien():
    while True:
        print("\n===== MENU QUẢN LÝ NHÂN VIÊN =====")
        print("1. Y1 - Nhập danh sách và lưu file")
        print("2. Y2 - Đọc từ file và xuất")
        print("3. Y3 - Tìm nhân viên theo mã")
        print("4. Y4 - Xóa nhân viên theo mã (cập nhật file)")
        print("5. Y5 - Cập nhật nhân viên theo mã (ghi file)")
        print("6. Y6 - Tìm nhân viên theo khoảng lương")
        print("7. Y7 - Sắp xếp theo họ và tên")
        print("8. Y8 - Sắp xếp theo thu nhập")
        print("9. Y9 - Top 5 nhân viên thu nhập cao nhất")
        print("0. Thoát")
        print("===================================")

        chon = input("Nhập lựa chọn (0-9): ").strip()

        if chon == "0":
            print("Tạm biệt!")
            break
        elif chon == "1":
            nhap_danh_sach()
        elif chon == "2":
            doc_tu_file()
        elif chon == "3":
            tim_theo_ma()
        elif chon == "4":
            xoa_theo_ma()
        elif chon == "5":
            cap_nhat_nhan_vien()
        elif chon == "6":
            tim_theo_luong()
        elif chon == "7":
            sap_xep_ten()
        elif chon == "8":
            sap_xep_thu_nhap()
        elif chon == "9":
            top_5_thu_nhap()
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
