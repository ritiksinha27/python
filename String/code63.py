#Write a Python program to remove leading zeros from an IP address
'''S='02.245'
L=[]
y=''
L=S.split('.')
for i in L:
    y+=i.strip('0')
print(y)
'''
ip_add='020.0.242.1.10'
new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])  
print(new_ip_add)

ip add