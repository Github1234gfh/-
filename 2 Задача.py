# 2 Задача
l=[]
print('Чтобы закончить ввод намера введите "."')
while True:
	a=input('Ввод номеров ')
	b=a.split()
	if a=='.':
		break
	l+=b
n=0
print('ГРЗ типа 1А:')
while n<len(l):
	if len(l[n])==8 or len(l[n])==9:
		b=l[n]
		if b[0].isalpha()==True and b[1].isdigit()==True and b[2].isdigit()==True and b[3].isdigit()==True and b[4].isalpha()==True and b[5].isalpha()==True and b[6].isdigit()==True and b[7].isdigit()==True:
			print(b)
	n+=1
