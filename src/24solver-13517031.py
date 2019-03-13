#Karina Iswara/13517031

import time

def enumNum(i,num,numx):
#untuk meng-enumerasi angka
	numx = num[:]
	i = num[i]
	num.remove(i)
	return i,numx

def enumOpt(i):
#untuk meng-enumerasi operator
	if i == 0:
		i = '+'
	elif i == 1 :
		i = '-'
	elif i == 2 :
		i = '*'
	elif i == 3 :
		i = '/'
	return i

def count(list_answer,equation):
#untuk menghitung apakah persamaan bernilai 24, jika iya akan mengecek apakah
#persamaan tersebut sudah ada dalam list_answer, jika tidak akan dimasukan ke dalam list
	try :
		result = eval(equation)
	except ZeroDivisionError:
		result =0
	if result == 24 :
		i = 1
		found = 0
		while i<= len(list_answer) and found == 0 :
			if equation == list_answer[i-1] :
				found = 1
			i = i + 1
		if found == 0:
			list_answer.append(equation)
	return list_answer

#Main Program
start = time.time() #untuk menghitung waktu eksekusi program
num = input('Input 4 postive integers : ').split()
list_answer = []
num4,num3,num2 = [],[],[]

for i in range(4):
	i,num4 = enumNum(i,num,num4)
	for j in range(3):
		j,num3 = enumNum(j,num,num3)
		for k in range(2) :
			k,num2 = enumNum(k,num,num2)
			l = num[0]
			for x in range(4) :
				x = enumOpt(x)
				for y in range(4) :
					y = enumOpt(y)
					for z in range(4) :
						z = enumOpt(z)
						equation = str('(('+i+x+j+')'+y+k+')'+z +l)
						list_answer = count(list_answer,equation)
						equation = str('('+i+x+'('+j+y+k+'))'+z+l)
						list_answer = count(list_answer,equation)
						equation = str(i+x+'(('+j+y+k+')'+z+l+')')
						list_answer = count(list_answer,equation)
						equation = str('('+i+x+j+')'+y+'('+k+z+l+')')
						list_answer = count(list_answer,equation)
			num =num2[:]
		num = num3[:]
	num = num4[:]

#Print hasil jawaban
if len(list_answer) == 0:
	print ('No Solution Found')
else :
	print(len(list_answer),' Solution(s) found : ')
	j = 1
	for i in list_answer:
		print(j,'. ',i)
		j = j +1
end = time.time()
print('time = ', end-start)