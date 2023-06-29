n = int(input("Nhap n: "))
x = int(input("Nhap x: "))
kq = float(-1)
tu = 1
mau = 1
dau = 1
for i in range(2,2*n+1,2) :
    tu = tu * x * x
    mau = mau * i * (i-1)
    kq = kq + dau * float(tu/mau)
    dau = -dau
print("Ket qua la: ",kq)
