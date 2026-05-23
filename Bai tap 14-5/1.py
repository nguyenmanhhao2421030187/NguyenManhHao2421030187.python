n = int(input("Nhập n = "))
x = []

for i in range(n):
    a = float(input(f"Nhập x[{i+1}] = "))
    x.append(a)

tong = 0
dem = 0

for i in range(n):
    if -1000 < x[i] < -10:
        tong = tong + x[i]
        dem = dem + 1

if dem > 0:
    tbc = tong / dem
    print("Trung bình cộng các phần tử âm trong khoảng (-1000, -10) là:", tbc)
else:
    print("Không có phần tử nào thỏa điều kiện.")
