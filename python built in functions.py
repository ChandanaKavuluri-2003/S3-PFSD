class Student:
    def __init__(self, id, name, cgpa):
        self.id = id
        self.name = name
        self.cgpa = cgpa


s = Student(10, "chandana", 9.9)
print(getattr(s, "name"))
setattr(s, "id", 11)
print(getattr(s, "id"))
delattr(s, "id")
# print(getattr(s,"id")) #error
print(hasattr(s, "name"))