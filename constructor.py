#parametrized
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
def display(self):
    print(self.id, self.name)
s1 = Student(10, "abc")
s2 = Student(20, "def")  # when we create an object constructor will automatically called.
s1.display()
s2.display()
#non parametrized
class Student:
    def __init__(self):
        print("first")

    def __init__(self):
        print("second")


std = Student()  # In python last constructor will get invoked.