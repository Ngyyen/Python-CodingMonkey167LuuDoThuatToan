n = int(input("Nhap n: "))
s = 0
for i in range(1,n+1) :
    s += 1/(i*(i+1)*(i+2))
print("Ket qua:", s)
