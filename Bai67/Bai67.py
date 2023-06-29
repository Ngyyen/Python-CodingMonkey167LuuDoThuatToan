n = int(input("Nhap n: "))
flag = 0
t = int(n)
while t > 0 :
    dv = t % 10
    if dv % 2 == 1 : 
        flag = 1
        break
    t = t // 10
if flag == 1 :
    print("")
