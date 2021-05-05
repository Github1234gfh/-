# Python 1 задача
import random 
n=int(input('Введите n '))
l=[]
b=[]
c=0
a=0
d=0
ga=0
max=-100.0
min=100.0
for i in range(n):
	b=[]
	b.append(random.randint(-100, 100))
	b.append(random.randint(-100, 100))
	l.append(b)
for j in range(0,n):
	c=l[j]
	a=(c[0]**2+c[1]**2)**0.5
	if a>max:
		max=a
	if a<min:
		min=a
	d+=a
print('Начальные координаты:',*l)
print('')
print('Среднее = '+str(d/n))
print('Минимальное = '+str(min))
print('Максимальное = '+str(max)+'\n')
count=0
count2=0
for g in range(0,n):
	per=l[g]
	if per[0]>0 and per[1]>0:
		ga1=per
		l.remove(per)
		l.insert(0, ga1)
		count+=1
for g in range(0,n):
	per=l[g]
	if per[0]<0 and per[1]>0:
		ga2=per
		l.remove(per)
		l.insert(count,ga2)
		count2+=1
for g in range(0,n):
	per=l[g]
	if per[0]<0 and per[1]<0:
		ga3=per
		l.remove(per)
		l.insert(count2+count, ga3)
for g in range(0,n):
	per=l[g]
	if per[0]>0 and per[1]<0:
		ga4=per
		l.remove(per)
		l.append(ga4)
print('Сортированные координаты:',*l)
print('Сортированно было по условию "Расположить точки в порядке обхода против часов стрелки, начиная с точки, ближайшей к оси у, лежащей в координатном углу I (положительные абсциссы и ординаты), если есть таковые"')
