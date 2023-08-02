#Write a Python program to find string similarity between two given strings.
'''def similar():
    S1=input("Enter the string 1 =")
    S2=input("Enter the strig 2 =")
    x=''
    for i in S1:
        if i in S2 :
            x+=i
            
    print(x)
    if len(S1)>len(S2):
        y=len(x)/len(S1)
    else:
        y=len(x)/len(S2)
    print(y)
similar()'''

def similar():
    import difflib
    str1=input("enter string 1 =")
    str2=input("enter string 2 =")
    result =  difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
    print(result.ratio())
similar()