#baikt cau_3
n= intput("nhập n:")
tich =  1
for i in n:
    tich *= int (i)

if tich % 2 == 0 and tich > 20:
    print ("thoả mãn điều kiện")
else:
    print ("không thỏa mãn điều kiện")