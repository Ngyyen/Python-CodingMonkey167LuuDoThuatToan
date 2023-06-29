n = int(input("Nhap n: "))
i = 0
flag = 0
while i * i <= n :
    if i * i == n :
        flag = 1
        break
    i += 1
if flag == 1 :
    print("n la so chinh phuong")
else :
    print("n khong la so chinh phuong")
