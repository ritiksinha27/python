'''Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'''

s=input("enter the string")
x=0
y=0
for i in range(len(s)):
    if s[i:i+3]=='not':
        x=i 
    if s[i:i+4]=='poor':
        y=i
if x<y:
    print(s[:x]+'good'+s[y+4:])