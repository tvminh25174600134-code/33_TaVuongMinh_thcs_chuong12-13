with open("nguon.dat", "rb") as f_nguon:
    with open("dich.dat", "wb") as f_dich:
        while True:
            data = f_nguon.read(1024)
            if not data:
                break
            f_dich.write(data)
print("Đã sao chép file thành công.")
