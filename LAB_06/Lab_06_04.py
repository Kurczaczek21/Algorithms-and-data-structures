import random
from time import time
from Lab_06_02 import Trees

if __name__ == '__main__':
	number_of_elements = [50, 100, 500, 1_000, 10_000, 25_000, 50_000, 100_000, 250_000, 1_000_000]

	data = []
	current=0

	for element in number_of_elements:
		elems_to_insert = [round(random.uniform(.00, 10.00), 2) for _ in range(element)]

		trees = Trees(10)

		ACCURACY = 100_000  # variable on CAPS-LOCK = constance !!!

		insert_start = time()
		for elem in elems_to_insert:
			trees.insert(elem, False)  # insert elems to tree
		insert_end = time()

		min_start = time()
		for i in range(ACCURACY):
			minimum = trees.min(2)  # minimum in third tree
		min_end = time()

		max_start = time()
		for i in range(ACCURACY):
			maximum = trees.max(2)  # maximum in third tree
		max_end = time()

		random_float = round(random.uniform(.0, element / 2), 2)

		search_start = time()
		for i in range(ACCURACY):
			search = trees.search(random_float)
		search_end = time()

		data.append([
			element,
			(insert_end - insert_start),
			(min_end - min_start) / ACCURACY,
			(max_end - max_start) / ACCURACY,
			(search_end - search_start) / ACCURACY
		])

		print(
			'for '+str(element)+' elements: \n'
			'insertion time: '+str(data[current][1])+'\n'
			'seraching for minimum time: '+str(data[current][2])+'\n'+
			'searching for maximum time: '+str(data[current][3])+'\n'+
			'seraching specific element time: '+str(data[current][4])+'\n'			
			)
		current+=1