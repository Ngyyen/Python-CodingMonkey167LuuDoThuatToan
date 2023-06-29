import math
n = int(input("Nhap n: "))
x = int(input("Nhap x: "))
kq = float(0)
soHang = 1
for i in range(1,n+1) :
    soHang *= x
    kq = math.sqrt(soHang + kq)
print("Ket qua la: ",kq)
