n = int(input("Nhập n = "))
x = []

for i in range(n):
    a = int(input(f"Nhập x[{i+1}] = "))
    x.append(a)

tong = 0

for i in range(n):
    if x[i] % 2 == 0:
        tong = tong + x[i]

print("Tổng các phần tử chẵn:", tong)

if tong % 7 == 0 and tong < 200:
    print("Tổng chia hết cho 7 VÀ nhỏ hơn 200.")
elif tong % 7 == 0:
    print("Tổng chia hết cho 7 nhưng KHÔNG nhỏ hơn 200.")
elif tong < 200:
    print("Tổng nhỏ hơn 200 nhưng KHÔNG chia hết cho 7.")
else:
    print("Tổng KHÔNG chia hết cho 7 và KHÔNG nhỏ hơn 200.")
