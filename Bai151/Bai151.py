n = int(input("Nhap n: "))
t = n
flag = 1
while t > 1 :
    dv = t % 2
    if dv == 1 :
        flag = 0
        break
    t = t / 2
if flag == 1 :
    print("n co dang 2^m")
else :
    print("n khong co dang 2^m")
