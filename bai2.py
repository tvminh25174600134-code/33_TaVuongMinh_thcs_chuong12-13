with open("vanban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
cac_tu = noi_dung.split()
tan_suat = {}
for tu in cac_tu:
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1
print("Tần suất xuất hiện của các từ:")
for tu, so_lan in tan_suat.items():
    print(tu, ":", so_lan)
