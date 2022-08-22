class ABC:
    def info(self,id=10):
        self.id=id
        return id
ob=ABC()
print(ob.info())
print(ob.info(20))
print("----Method overriding-----")
class Student:
    def add(self,n1,n2):
        return (n1+n2)
class Student2(Student):
    def add(self,n1,n2):
        return (n1+n2)
s=Student2()
print(s.add(10,20))
print(s.add(10,30))
