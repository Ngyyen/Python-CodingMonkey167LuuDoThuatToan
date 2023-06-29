kq = float(1)
soHang = float(1)
giaiThua = 1
i = 1
while soHang >= 0.000001 :
    giaiThua *= i
    soHang = 1 / giaiThua
    kq = kq + soHang
    i += 1
print("Ket qua la: ",kq)
