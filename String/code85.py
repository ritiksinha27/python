#Write a Python program to convert a given Bytearray to a Hexadecimal string.

def hexa():
        S=input("Enter  the number =")
        L=S.split(',')
        print(L)
        
        result=''.join('{:02x}'.format(int(x)) for x in L )
        print(result)

hexa()