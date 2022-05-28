class Item:
    def __init__(self, width,height,value) -> None:
        self.width=width
        self.height=height
        self.value=value

    def surface_area(self):
        return self.width*self.height
    
    def get_value(self):
        return self.value
    
    def rotate(self):
        x=self.width
        self.width=self.height
        self.height=x
    
    def printer(self):
        print(self.value,self.width,self.height)

    def proportion(self):
        return self.value/(self.width*self.height)

pan=Item(1,30,69)
pan.printer()
pan.rotate()
pan.printer()
print(pan.proportion())