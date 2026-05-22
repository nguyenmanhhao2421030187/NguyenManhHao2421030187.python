#baikt cau_2
n=input("nhập n:")
tong=0
for i in n:
    tong+=int(i)
if tong % 3 == 0:
    print("chia hết cho 3")
else:
    print("không chia hết cho 3")