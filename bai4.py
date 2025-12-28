with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("ID,Ten san pham,Gia\n")
    f.write("1,Laptop,1200\n")
    f.write("2,Chuot may tinh,25\n")
    f.write("3,Ban phim,75\n")
id_can_sua = input("Nhập ID sản phẩm: ")
gia_moi = input("Nhập giá mới: ")
dong_moi = []
with open("san_pham.txt", "r", encoding="utf-8") as f:
    for dong in f:
        if dong.startswith(id_can_sua + ","):
            parts = dong.strip().split(",")
            parts[2] = gia_moi
            dong = ",".join(parts) + "\n"
        dong_moi.append(dong)
with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.writelines(dong_moi)
print("Đã cập nhật giá sản phẩm.")
