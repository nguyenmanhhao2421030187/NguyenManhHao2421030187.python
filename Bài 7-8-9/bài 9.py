#bai_9
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

tong = a + b + c
dem_chan = 0

for i in str(tong):
    if int(i) % 2 == 0:
        dem_chan += 1

print("Tổng:", tong)
print("Số lượng chữ số chẵn trong tổng:", dem_chan)