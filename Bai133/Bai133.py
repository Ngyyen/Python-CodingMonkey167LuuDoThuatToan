x = float(input("Nhap x: "))
y = float(input("Nhap y: "))
z = float(input("Nhap z: "))
if x + y > z and x + z > y and y + z > x :
	if x**2 == y**2 + z**2 or y**2 == x**2 + z**2 or z**2 == x**2 + y**2 :
		if x == y or x == z or y == z :
				print("Tam giac vuong can")
		else :
				print("Tam giac vuong")
	else :
		if x == y or x == z or y == z :
			if x == y and y == z :
				print("Tam giac deu")
			else :
				print("Tam giac can")
		else :
			print("Tam giac thuong")
else :
	print("Khong la tam giac")
