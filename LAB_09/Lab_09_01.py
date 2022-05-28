import operator

class Item:
    def __init__(self,id:int, width:int,height:int,value:int) -> None:
        self.id=id
        self.width=width
        self.height=height
        self.value=value

    def surface_area(self):
        return self.width*self.height

    def get_id(self):
        return self.id
    
    def get_value(self):
        return self.value
    
    def rotate(self):
        x=self.width
        self.width=self.height
        self.height=x
    
    def printer(self):
        print(self.id,self.width,self.height,self.value)

    def proportion(self):
        return self.value/(self.width*self.height)

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
    sorted_elements = sorted(elements, key=operator.attrgetter('value'))    #????????



if __name__ == '__main__':
    items=open_file(20)
    items[25].printer()
    
    