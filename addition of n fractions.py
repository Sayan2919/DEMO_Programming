
# coding: utf-8

# In[4]:


class fraction:
    def __init__(self,num,den):
        self.num=num
        self.den=den
    #end __init__
    def lcm(self,x,y):
        if x > y:
            greater = x
        else:
            greater = y
        #end if
        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1
        #end while
        return lcm
    #end lcm
    def __add__(self, ob1):
        den=self.lcm(self.den,ob1.den)
        num=int(self.num * den/self.den + ob1.num * den/ob1.den)
        temp = fraction(num,den)
        return temp
    #end add
    def __str__(self):
        return '%s/%s'%(self.num,self.den)
#end class fraction
    


# In[5]:


def sumOfFrac(ls):
    s = fraction(0,1)
    for i in ls:
        s += i
    #end for
    return s


# In[6]:


n = int(input("Enter the limit: "))
ls = [0] * n
for i in range(n):
    a,b = map(int,input("Enter the numerator and denominator: ").split())
    t = fraction(a,b)
    ls[i] = t
#end for
out = sumOfFrac(ls)
print(out)

