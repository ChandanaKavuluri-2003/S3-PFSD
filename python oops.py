#class
class Student:
    id = 10
    name = "abc"
    def display():
        print(id, name)
#object
class Student:
    id = 10
    name = "abc"
    def display(self):
        print(self.id, self.name)
std=Student()
std.display()
#delete object
del std
#std.display()#error


