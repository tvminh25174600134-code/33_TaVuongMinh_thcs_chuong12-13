import csv
with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Ten", "Luong"])
    writer.writerow([1, "An", 60000])
    writer.writerow([2, "Binh", 45000])
    writer.writerow([3, "Chi", 70000])
with open("nhan_vien.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("Nhân viên có lương trên 50000:")
    for row in reader:
        if int(row["Luong"]) > 50000:
            print(row["ID"], row["Ten"], row["Luong"])
