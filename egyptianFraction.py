from math import gcd


class UnitFrac():
    def __init__(self,den):
        self.num = 1
        self.den = den
    #end __init__
    def __str__(self):
        return (str(self.num) + "/" + str(self.den))
    #end__str
#end class

def lcm(x,y):
    return (x * y) // gcd(x,y)
#lcm


class Fraction():
    def __init__(self,num,den):
        self.num=num
        self.den=den
    #end __init__
    
    def __add__(self,ob1):
        den=lcm(self.den,ob1.den)
        num=int(self.num * den/self.den + ob1.num * den/ob1.den)
        temp = Fraction(num,den)
        return temp
    #end __add__
    def normalise(self):
        hcf = gcd(self.num,self.den)
        self.num /= hcf
        self.den /= hcf
    #normalise
    def __sub__(self,a):
        den=lcm(self.den,a)
        num=int(self.num * den/self.den - 1 * den)
        temp = Fraction(num,den)
        return temp
    #end sub
    def __str__(self):
        return (str(int(self.num)) + "/" + str(int(self.den)))
    #end__str
#end class    

def sumOfFrac(ls):
    s = Fraction(0,1)
    for i in ls:
        s += i
    #end for
    s.normalise()
    return s


n = int(input("Enter the number of egyption fraction: "))
ls = [0] * n
for i in range(n):
    ls[i] = UnitFrac(int(input("Enter the denominator: ")))
#end for
for i in range(n-1):
    print(ls[i],end="+")
#end for
print(ls[n-1],end="=")
output = sumOfFrac(ls)
print(output)

