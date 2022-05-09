from Lab_06_02 import Trees

if __name__ == '__main__':

#   task no 1 

	elems_to_insert = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]

	trees = Trees()
	for elem in elems_to_insert:
		trees.insert(elem)

	trees.print()

#   task no 2
	for elem in elems_to_insert:
		trees.insert(elem)

   # trees.print()

	print(
		str(trees.min(2))+'	'+  # MIN on third tree
		str(trees.max(2))+'	'+  # MAX on third tree
		str(trees.search(7.7))+'	',  # SEARCH
		sep='\n'
	)
