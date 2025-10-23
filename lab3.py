# lab3_basic.py
def main():
    print("=== MÁY TÍNH CƠ BẢN ===")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("0. Thoát")

    while True:
        lua_chon = input("\nChọn phép tính (0-4): ")

        if lua_chon == "0":
            print("Thoát chương trình.")
            break

        # nhập 2 số
        try:
            a = float(input("Nhập số thứ nhất: "))
            b = float(input("Nhập số thứ hai: "))
        except ValueError:
            print(" Vui lòng nhập số hợp lệ!")
            continue

        # xử lý phép tính
        if lua_chon == "1":
            print(f"{a} + {b} = {a + b}")
        elif lua_chon == "2":
            print(f"{a} - {b} = {a - b}")
        elif lua_chon == "3":
            print(f"{a} × {b} = {a * b}")
        elif lua_chon == "4":
            if b != 0:
                print(f"{a} ÷ {b} = {a / b}")
            else:
                print(" Không thể chia cho 0!")
        else:
            print(" Vui lòng chọn đúng số trong menu!")

