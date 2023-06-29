k = int(input("Nhap k: "))
att = -1
at = 3
i = 2
ahh = 0
while i <= k :
	ahh = 5 * at + 6 * att;
	i = i + 1;
	att = at;
	at = ahh;
print("Ket qua la: ", ahh)
