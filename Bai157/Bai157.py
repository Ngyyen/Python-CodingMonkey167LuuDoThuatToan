n = int(input("Nhap n: "))
s = 0
for i in range(1,n+1) :
    s += float(1/i)
    print("a(",i,") =", s)
