f = open("C:\\Users\\Serm\\github.com\\advent-of-code-2022\\02_input.txt")
lines = f.read().split('\n')
#a=ค้อน b=กระดาษ c=กรรไกร
tab = {}
tab['AX'] = 3 + 0
tab['AY'] = 1 + 3
tab['AZ'] = 2 + 6
tab['BX'] = 1 + 0
tab['BY'] = 2 + 3
tab['BZ'] = 3 + 6
tab['CX'] = 2 + 0
tab['CY'] = 3 + 3
tab['CZ'] = 1 + 6

myscore = 0
for line in lines:
	if line != '':
		key = line.replace(' ', '')
		myscore += tab[key]

print(myscore)
f.close()