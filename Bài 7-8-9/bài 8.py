#bai_8
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
z = int(input("Nhập z: "))

tich = x * y * z
chuoi_tich = str(tich)

so_chu_so = len(chuoi_tich)
lon_nhat = max(chuoi_tich)

print("Tích:", tich)
print("Số lượng chữ số:", so_chu_so)
print("Chữ số lớn nhất:", lon_nhat)