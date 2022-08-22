#numbers-int,float,complex
a=10
print(a,type(a))
b=10.5
print(b,type(b))
c=10+4j
print(c,type(c))
#sequence type-string,lists,tuple
s1="hello"
s2="welcome to class"
print(s1[3],s2[9],s1[0:4],s2[0:11],s2[:9],s1[1:],s2[9:],type(s1))
list1=[5,"chandana",9.9,10]
print(list1,list1[1],list1[0:3],list1[1:],list1[:3])
print(list1*2)
print(list1+list1)
print(type(list1))
tuple1=(5,"Hello","Chandana",9.9)
print(tuple1,tuple1[1:3],tuple[2:])
print(tuple1*2)
print(tuple1+tuple1)
print(type(tuple1))
#dictionary
dic={1:"ABC",2:"DEF",3:"GHI"}
print(dic)
print(dic[1])
print(dic.keys())
print(dic.values())
dic.clear()#output={}
del dic
#Set
set1 = set()
set2={5,"Hello","chandana",9.9}
print(set2)#(order will change)
set2.add(10)
print(set2)
set2.remove(2)#value 2
set2.clear()
del set2


