n = int(input("Nhap n: "))
kq = 0
giaiThua = 1
for i in range(1,n+1) :
    giaiThua *= i
    kq = kq + i * giaiThua
print("Ket qua la: ",kq)
