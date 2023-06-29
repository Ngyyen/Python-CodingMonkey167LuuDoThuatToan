n = int(input("Nhap n: "))
dem = 0
t = int(n)
while t > 0 :
    dv = t % 10
    if dv % 2 == 1 : 
        dem += 1
    t = t // 10
print("So chu so le cua n: ", dem)
