#Write a Python program to select an item randomly from a list.
def random():
    import random
    
    L=[x for x in input("Enter the list =").split(',')]
    ran=random.choice(L)
    print(ran)

random()

