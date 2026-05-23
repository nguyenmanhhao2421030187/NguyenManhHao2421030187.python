a = int(input("Nhập a = "))
b = int(input("Nhập b = "))

# Tìm chữ số nhỏ nhất của b
nho_nhat = 9
temp = b
while temp > 0:
    chu_so = temp % 10
    if chu_so < nho_nhat:
        nho_nhat = chu_so
    temp = temp // 10

print("Chữ số nhỏ nhất của b là:", nho_nhat)

if nho_nhat == 0:
    print("Chữ số nhỏ nhất là 0, không thể chia.")
elif a % nho_nhat == 0:
    print(a, "chia hết cho", nho_nhat)
else:
    print(a, "không chia hết cho", nho_nhat)
