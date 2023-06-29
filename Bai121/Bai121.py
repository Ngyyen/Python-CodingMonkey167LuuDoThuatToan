k = int(input("Nhap k: "))
att = 1
at = 1
i = 2
ahh = 0
while i <= k :
	ahh = at + att;
	i = i + 1;
	att = at;
	at = ahh;
print("Ket qua la: ", ahh)
