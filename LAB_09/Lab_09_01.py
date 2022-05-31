import operator
import numpy as np
from time import time

class Item:
    def __init__(self,id:int, width:int,height:int,value:int) -> None:
        self.id=id
        self.width=width
        self.height=height
        self.value=value
        self.proportion =self.value/(self.width*self.height)
        
    def __str__(self):
        return str(self.id)

    def surface_area(self):
        return self.width*self.height

    def get_id(self):
        return self.id

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
    
    def get_value(self):
        return self.value
    
    def rotate(self):
        self.width,self.height =self.height, self.width
    
    def printer(self):
        print(self.id,self.width,self.height,self.value,self.proportion)

def open_file(data:int):
    """opens file with items
    """
    file=open('C:\PY prog\LAB_09\packages\packages'+str(data)+'.txt','r').readlines()
    items=[]
    file.pop(0) 
    file.pop(0)
    for i in range(len(file)):    
        file[i]=file[i].split(',')
        items.append(Item(int(file[i][0]),int(file[i][1]),int(file[i][2]),int(file[i][3])))

    return items

def sort_by_values(elements:list):
    return sorted(elements , key=operator.attrgetter('proportion'),reverse=True)

def check_fit(x, y, backapck):
	"""
	:return: False if element does not fit to knapsack
				else tuple of starting coordinates and boolean determining if element was turned (x, y, True/False)
	"""
	for x_start in range(len(backapck) - x + 1):
		for y_start in range(len(backapck) - y + 1):
			fits = True
			for x_iter in range(x):
				for y_iter in range(y):
					if backapck[x_start + x_iter][y_start + y_iter] != 0:
						fits = False
						break
				if not fits:
					break
			if fits:
				return x_start, y_start, False

	# other orientation
	for x_start in range(len(backapck) - x + 1):
		for y_start in range(len(backapck) - y + 1):
			fits = True
			for x_iter in range(x):
				for y_iter in range(y):
					if backapck[y_start + y_iter][x_start + x_iter] != 0:
						fits = False
						break
				if not fits:
					break
			if fits:
				return x_start, y_start, True

	return False

if __name__ == '__main__':
    items=open_file(20)
    items=sort_by_values(items)
    for item in items:
        item.printer()

    backapck = np.zeros((20, 20), dtype=int)
    value=0
    start=time()
    
    for item in items:
        fit = check_fit(item.get_width(), item.get_height(), backapck)
        if fit:
            # def x_y_placement(width,height):
                

            if (fit[2]):   # x_start   width + x_start
                for x in range(fit[0], item.get_width() + fit[0]):
                    #             y_start   height + y_start
                    for y in range(fit[1], item.get_height() + fit[1]):
                        backapck[y][x] = item.get_id()
            # x,y placement
            if (fit[2]):   # x_start   width + x_start
                for x in range(fit[0], item.get_width() + fit[0]):
                    #             y_start   height + y_start
                    for y in range(fit[1], item.get_height() + fit[1]):
                        backapck[y][x] = item.get_id()  # insert item with `id` to knapsack
            # y,x placement
            else:
                for x in range(fit[0], item.get_width() + fit[0]):
                    for y in range(fit[1], item.get_height() + fit[1]):
                        backapck[x][y] = item.get_id()  # insert item with `id` to knapsack

            value += item.get_value()
    
    # value of all elements
    max_value = 0
    for item in items:
        max_value += item.get_value()

    # print(knapsack)
    elapsed_time = time() - start
    print(f'size = {20}')
    print(f'time = {elapsed_time}')
    print(f'reached value = {value}')
    print(f'max possible value = {max_value}\n')
    print(backapck)
    