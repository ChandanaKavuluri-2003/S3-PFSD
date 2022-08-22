#import calculator
#print(sum(10, 20))
import math
print(math.sqrt(25))
print(math.factorial(13))
from datetime import datetime

a = datetime.now()  # now displays current date and time
print(a)
print(a.year)  # only year
x=min(5,15,10) #we can call directly without using module_name. in math
y=max(5,15,10)
print(x)
print(y)
import re
a="in KLU at KLU"
b=re.findall(r"KL",a) #findall is a func
print(b)
c=re.search(r"i",a)
print(c)
s=" "
print(re.split(s,a))
s1="\D"
print(re.sub(s1,' ',a))