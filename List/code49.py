# Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', '
# color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

def listtod():
    inputlist=[(x) for x in input("Enter the list =").split(',') ]
    x=''
    for i in inputlist:
        for j in i:
            if j.isidentifier()==True or j==',' :
                print(j)
                x+=(j)
    print(x)
    
    
listtod()