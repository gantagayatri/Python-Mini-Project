#lab session is only one hour and one lab is there we need to give three timing slots for each section
#if any two lab sections are same we need to give prior to the first section
#example: sec-A lab time:10 , sec-B lab time:10 and sec-C lab time:11 
#then we need to give permission to A and schedule the other timing for sec-B which is not equal to sec-A nad sec-C
class Clas(object):
    def __init__(self,name1):
        self.name1=name1
    def display(self):
        print(self.name1)
    def secA(self):
        li=[]
        print("enter the three timings of the lab for sec-A")
        for i in range(0,3):
            ele=int(input())
            li.append(ele)
        print(li)
    def secB(self):
        li1=[]
        print("enter the three timings of the lab for sec-B")
        for j in range(0,3):
            ele=int(input())
            li1.append(ele)
        print(li1)
    def secC(self):
        li2=[]
        print("enter the three timings of the lab for sec-C")
        for k in range(0,3):
            ele=int(input())
            li2.append(ele)
        print(li2)
    
class Clas1(Clas):
    def __init__(self,name1,name2):
        self.name1=name1
        self.name2=name2
        Clas.__init__(self,name1)
    def secABC(self):
        a=int(input("enter the timing of sec-A"))
        b=int(input("enter the timing of sec-B"))
        c=int(input("enter the timing of sec-C"))
        if a==b==c:
            print("b and c not allowed because a already there. b and c schedule another time")
        elif a==b and a!=c:
            print("b not allowed, because a already there b should schedule another time ")
        elif a!=b and a!=c:
            print("a allowed")
        else:
            print("nothing")
    def mnq(self):
        li3=[]
        li4=[]
        n=int(input("enter students"))
        for i in range(1,n):
            li3.append(i)
        print(li3)
        m=int(input("enter chairs"))
        for j in range(1,m):
            li4.append(j)
        print(li4)
        zipi=zip(li3,li4)
        uvx=dict(zipi)
        print(uvx)
obj1=Clas1("parent class","child class")
obj1.display()
obj=Clas("Parent class")
obj.secA()
obj.secB()
obj.secC()
obj1.secABC()
obj1.mnq()