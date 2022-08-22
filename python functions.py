#in-buit
a=input("Enter Number")
print(a)
#user defined
def add(num1, num2):
    return num1 + num2
print(add(5, 2))
#function arguements
#default arguements
def sample(num1, num2=10):
    print(num1)
    print(num2)


sample(5)
sample(5, 20)  # it prints 5 and 20
#keyword arguements
def sample(num1, num2=10):
    print(num1)
    print(num2)


sample(num1=20, num2=5)
#required arguements
def sample(num1, num2):
    print(num1)
    print(num2)


sample(5, 4)


