class PalindromeTrawler:
    def __init__(self,string):
        self.string=string
    #end__init__
    def checkPalindrome(self,st):
        flag = False
        revs="".join(reversed(st))
        if(st == revs):
            flag = True
        #end if
        return flag
    #end checkPalindrome

n=int(input())
while(n!=0):
    l=int(input())
    p = PalindromeTrawler(input())
    for i in range(l):
        for j in range(i+3,l+1):
            if(p.checkPalindrome(p.string[i:j])):
                print(i+1," ",p.string[i:j])
            #end if
        #end for
    #end for
    n=n-1
#end while

