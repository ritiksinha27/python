import re
S='abcdebcxsdfsfsfbcsffdbc'
p='bc'
x=re.finditer(p,S)
for i in x:
    print(i)