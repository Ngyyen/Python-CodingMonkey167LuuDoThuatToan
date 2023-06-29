kq = float(0)
soHang = float(1)
i = 1
while soHang >= 0.000001 :
    soHang = 1 / i
    kq = kq + soHang
    i += 2
print("Ket qua la: ",kq)
