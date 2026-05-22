#baikt cau_5
m= int(input("nhập m:"))
n=int(input("nhập n:"))
tong_n = 0
for i in n:
    tong_n += int(i)

if tong_n != 0 and m % tong_n ==0:
    print ("chia hết")
else:
    print ("không chia hết")