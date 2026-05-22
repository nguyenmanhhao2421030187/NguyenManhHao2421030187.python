# kiểm tra a có chia hết cho chữ số của b
a = int(input("Nhập a: "))
b = input("Nhập b: ")

chu_so_nho_nhat = int(min(b))

if chu_so_nho_nhat == 0:
    print("Chữ số nhỏ nhất là 0, không thể chia cho 0.")
elif a % chu_so_nho_nhat == 0:
    print("Chia hết")
else:
    print("Không chia hết") 