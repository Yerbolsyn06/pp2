###REGEX
##1
import re
txt=input()
l=txt.split()

for i in l:
    s=re.findall("^ab*",i)
    if s:
        print(i)
##2
import re
txt=input()
l=txt.split()

for i in l:
    s=re.findall("^abb",i)
    if s:
        print(i)
for i in l:
    s=re.findall("^abbb",i)
##3
import re
import re
txt=input()
l=txt.split()


for i in l:
    s=re.findall("^[a-z]_[a-z]",i)
    if s:
        print(i)
##4
import re
txt=input()
l=txt.split()

for i in l:
    s=re.findall("^[A-Z][a-z]",i)
    if s:
        print(i)
##5
import re
txt=input()
l=txt.split()

for i in l:
    s=re.findall("a.+b",i)
    if s:
        print(i)
##6
import re
txt="my name is ALmir"
q=re.sub("[ ,.]",":",txt)
print(q)
##7


import re
txt=input()
l=txt.split("_")  

print(l[0], end="")
for i in range(1, len(l)):
    print(l[i].capitalize(), end="")
print(l)

##8
import re
txt = input()
l = re.split('[A-Z]', txt)
l=txt.split('[A-Z]')

print(l)
for i in range(0, len(l)):
    print(l[i], end="")
##9
import re
txt=input()

x=re.sub(r"( )([A-Z])",r"\1 \2",txt)
print(x)

##10

import re
txt=input()

x=re.sub(r"(\w)([A-Z])",r"\1_\2",txt)
s=x.lower()
print(s)



