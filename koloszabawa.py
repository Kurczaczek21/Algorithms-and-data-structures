from random import randint
class LOTTO:
	def __init__(self, list_len):
		if list_len<5 or list_len>6:
			raise ValueError('po chsa to nie zadziala')
		list=[]
		for i in range(list_len):
			list.append(randint(0,48))
		self.list=list

	def printer(self):
		return self.list

def SPRAWDZ(list1, list2):
	counter=0
	for i in range(len(list1)):
		for j in range(len(list2)):
			if list1[i]==list2[j]:
				counter+=1
	return counter

def SPRAWDZ2(list1, list2):
	for line in list1:
		if line in list2:
			print('jd jest 2 elementy')

lala = LOTTO(5)
papa = LOTTO(6)

print(SPRAWDZ(lala.printer(), papa.printer()))
print(SPRAWDZ(lala.list, papa.list))
SPRAWDZ2(lala.printer(), papa.printer())
print(lala.printer())

filename=str(lala.list[0])+str(lala.list[1])+'.txt'
file = open(filename,'w')
file.write(str(SPRAWDZ(lala.printer(), papa.printer()))+'AAAAAAAAAAAAAAAAAAAAS')
file.close