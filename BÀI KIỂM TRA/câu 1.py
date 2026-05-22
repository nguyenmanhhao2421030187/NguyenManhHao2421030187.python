#baikt cau_1
n=int(input("nhập n ":))
a=[]
for i in range(n):
    a.append(float(input(f"nhập phần tử thứ {i+1}:")))

tong=0
dem=0
for x in a:
    if 0<x<1000:
        tong+=x
        dem+=1
 
if dem>0:
    print ("trung bình cộng :",tong/dem)
else:
    print("Không có phần tử thỏa mãn")
