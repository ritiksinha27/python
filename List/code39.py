# Write a Python program to convert a list of multiple 
# integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

def integer():
    L=[x for x in input("Enter the list =")]
    finalL=''
    for i in L:
        if i.isnumeric()==True:
            finalL+=i
    
    print(int(finalL))
    
integer()