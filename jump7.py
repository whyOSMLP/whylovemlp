a = 0 
while a <= 99:
	a += 1 ##a每次+1直至=99
	if a % 7 == 0:##倍數除以7餘0爲7的倍數
	   continue
	elif a % 10 == 7:##個位上是7的數，即除以10餘7的數；
	   continue
	elif a // 10 == 7:##十位上是7的書，即除以10取整數爲7的數
	   continue
	print(a)
