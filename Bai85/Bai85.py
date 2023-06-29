n = int(input("Nhap n: "))
x = int(input("Nhap x: "))
kq = 0
dau = 1
soHang = 1
for i in range(1,n+1) :
    soHang *= x
    kq = kq + dau * soHang
    dau = -dau
print("Ket qua la: ",kq)
