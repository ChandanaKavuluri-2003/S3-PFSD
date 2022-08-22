class Parent:
    def fun(self):
        print("Parent class")


class Child(Parent):

    def fun1(self):
        print("Child class")


print("----Single Inheritance------")
ob = Child()
ob.fun()
ob.fun1()
print("-----Multi-level Inheritance-----")


class Parent1:
    def func1(self):
        print("1'st parent class")


class Intermediate(Parent1):
    def func2(self):
        print("Intermediate class")


class Derived(Intermediate):
    def func3(self):
        print("Derived class")


d = Derived()
d.func1()
d.func2()
d.func3()
print("-------Multiple Inheritance------")


class Base1:
    def fn(self):
        print("Parent class no.1")


class Base2:
    def fn1(self):
        print("Parent class no.2")


class CHild(Base1, Base2):
    def fn2(self):
        print("CHild Class")


cc = CHild()
cc.fn()
cc.fn1()
cc.fn2()
print("--------Hierarichal Inheritance-----")


class PARENT:
    def fn3(self):
        print("Hierarichal parent class")


class Derived1(PARENT):
    def fn4(self):
        print("Hierarichal child 1")


class Derived2(PARENT):
    def fn5(self):
        print("Hierarichal child 2")


dc = Derived1()
dc.fn3()
dc.fn4()
dc1 = Derived2()
dc1.fn3()
dc1.fn5()
print("--------Hybrid Inheritance--------")


class BASE:
    def function(self):
        print("Hybrid base class")


class CHILD1(BASE):
    def function1(self):
        print("hybrid derived class 1(hierarichal)")


class CHILD2(BASE):
    def function2(self):
        print("hybrid derived class 2(hierarichal)")


class CHILD3(CHILD1, CHILD2):
    def function3(self):
        print("hybrid derived class 3(multiple)")


cc = CHILD1()
# cc.function()
# cc.function1()
# cc1=CHILD2()
# cc1.function()
# cc1.function2()
cc2 = CHILD3()
cc2.function()
cc2.function1()
cc2.function2()
cc2.function3()

