n = int(input("Nhap n: "))
i = int(n / 2)
if n % 2 == 1 :
     print(n,"la uoc so le lon nhat cua",n)
else :
    while i >= 1 :
        if i % 2 == 1 and n % i == 0 :
            print(i,"la uoc so le lon nhat cua",n)
            break
        i = i - 1
