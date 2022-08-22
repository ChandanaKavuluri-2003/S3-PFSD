import math
class Rectangle:
    def areaRec(self,s1,s2):
        print(s1*s2)
    def periRec(self,s1,s2):
        print(2*(s1+s2))
class Circle:
    def circleArea(self,r):
        print(math.pi*r*r)
    def circlePer(self,r):
        print(2*math.pi*r)
class Triangle:
    def areaTriangle(self,a,b,c):
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(int(area))
    def periTriangle(self,a,b,c):
        print(a+b+c)
n=int(input("Enter 1 for circle 2 for rectangle 3 for triangle"))
if n==1:
    r=int(input("enter radius"))
    obj1=Circle()
    obj1.circleArea(r)
    obj1.circleArea(r)
if n==2:
    s1=int(input("enter side 1"))
    s2=int(input("enter side 2"))
    obj2=Rectangle()
    obj2.areaRec(s1,s2)
    obj2.periRec(s1,s2)
if n==3:
    a=int(input("enter side 1"))
    b=int(input("enter side 2"))
    c=int(input("enter side 3"))
    obj3=Triangle()
    obj3.areaTriangle(a,b,c)
    obj3.periTriangle(a,b,c)
