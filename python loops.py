#for
a=[1,2,3]
for x in a:
    print(x)
#while
i=1
while i<=10:
    print(i)
    i+=1
#while with exit
#other statements
#break
var = 10
while var > 0:
    print ('Current variable value :', var)
    var = var -1
    if var == 5:
        break

print ("Good bye!")
#continue
for letter in 'Python':
    # First Example
    if letter == 'h':
        continue
    print ('Current Letter :', letter)
#pass
a=5
if a<10:
    #we should not leave empty.
    pass
else:
    print("Invalid")
