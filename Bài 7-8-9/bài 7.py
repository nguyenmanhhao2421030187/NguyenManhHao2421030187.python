#bai_7
n = int(input("Nhập n: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

tong_nt = 0
for x in a:
    if x >= 2:
        is_prime = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            tong_nt += x

print("Tổng các số nguyên tố:", tong_nt)
if tong_nt % 2 != 0 and tong_nt > 50:
    print("Tổng là số lẻ và lớn hơn 50")
else:
    print("Không thỏa mãn điều kiện")