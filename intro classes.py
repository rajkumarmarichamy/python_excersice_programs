class Point:
    def __init__(self, x, y):  #constructor
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw') 


#point1 = Point()   #without constructor
point1 = Point(10, 20) # with constructor
print(point1.x)
#print(Point)