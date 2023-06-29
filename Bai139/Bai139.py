a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if a == 0 :
    if b == 0 : 
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else :
    print("Phuong tring co 1 nghiem:", float(-b/a))
