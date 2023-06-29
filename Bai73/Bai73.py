n = int(input("Nhap n: "))
x = int(input("Nhap x: "))
kq = float(0)
tu = 1
mau = 0
for i in range(1,n+1) :
    tu = tu * x
    mau = mau + i
    kq = kq + float(tu/mau)
print("Ket qua la: ",kq)
