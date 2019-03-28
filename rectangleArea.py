
# coding: utf-8

# In[ ]:


import math
class cords():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #end __init__


# In[ ]:


def length(x1,y1,x2,y2):
    l = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    return l
#end def


# In[ ]:


def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
#end slope


# In[ ]:


class area():
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    #end __init
    def calculateArea(self):
        m1 = slope(self.A.x, self.A.y, self.B.x, self.B.y)
        m2 = slope(self.A.x, self.A.y, self.C.x, self.C.y)
        m3 = slope(self.B.x, self.B.y, self.C.x, self.C.y)
        if(m1 * m2 == -1):
            l1 = length(self.A.x, self.A.y, self.B.x, self.B.y)
            l2 = length(self.A.x, self.A.y, self.C.x, self.C.y)
        elif(m2 * m3 == -1):
            l1 = length(self.A.x, self.A.y, self.C.x, self.C.y)
            l2 = length(self.B.x, self.B.y, self.C.x, self.C.y)
        else:
            l1 = length(self.A.x, self.A.y, self.B.x, self.B.y)
            l2 = length(self.B.x, self.B.y, self.C.x, self.C.y)
        #end if
        return l1 * l2


# In[ ]:


n = int(input("Enter the limit: "))
ls = [0] * n
for i in range(n):
    x1,y1,x2,y2,x3,y3=map(float,input("Enter the coordinates: ").split())
    ob1 = cords(x1,y1)
    ob2 = cords(x2,y2)
    ob3 = cords(x3,y3)
    ar = area(ob1,ob2,ob3)
    ls[i] = ar
#end for
for i in ls:
    print(i.calculateArea())
#end for
    
        
        

