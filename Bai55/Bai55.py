n = int(input("Nhap n: "))
s = 1
for i in range(1,n+1) :
    if n%i == 0 and i%2 == 1 :
        s = s*i
print("Tich cac uoc le cua n: ", s)
