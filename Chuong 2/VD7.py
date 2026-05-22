# vidu 7
toan = float(input("nhap diem toan:"))
ly = float(input("nhap diem ly:"))
hoa = float(input("nhap diem hoa:"))
dtb = (toan + ly + hoa) / 3
print("diem trung binh:", dtb)
if dtb < 5:
    print("xep loai:yeu")
elif dtb < 7:
    print("xep loai:trung binh")
elif dtb < 9:
    print("xep loai:kha")        
elif dtb <= 10:
    print("xep loai:gioi")
else:
    pass