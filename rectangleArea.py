import math
class cords():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #end __init__
#end class
def length(x1,y1,x2,y2):
    l = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    return l
#end def
def checkPythagoras(a,b,c):
    #import pdb
    #pdb.set_trace()
    if(abs((a*a + b*b) - c*c) < 0.0000001):
        return True
    else:
        return False
    #end if
#end checkPythagoras
class Rectangle():
    def __init__(self,a,b,c):
        self.cord1 = a
        self.cord2 = b
        self.cord3 = c
    #end __init
    def calculateArea(self):
        l1 = length(self.cord1.x, self.cord1.y, self.cord2.x, self.cord2.y)
        l2 = length(self.cord2.x, self.cord2.y, self.cord3.x, self.cord3.y)
        l3 = length(self.cord3.x, self.cord3.y, self.cord1.x, self.cord1.y)
        print(l1,l2,l3)
        if(checkPythagoras(l1,l2,l3)):
            l = l1 * l2
        elif(checkPythagoras(l2,l3,l1)):
            l = l2 * l3
        else:
            l = l3 * l1
        #end if
        return l
    #end calculateArea
n = int(input("Enter the limit: "))
ls = [0] * n
for i in range(n):
    x1,y1,x2,y2,x3,y3=map(float,input("Enter the coordinates: ").split())
    ob1 = cords(x1,y1)
    ob2 = cords(x2,y2)
    ob3 = cords(x3,y3)
    ar = Rectangle(ob1,ob2,ob3)
    ls[i] = ar
#end for
for i in ls:
    print(i.calculateArea())
#end for        

