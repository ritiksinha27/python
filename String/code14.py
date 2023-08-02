'''Write a Python function to create an HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>' '''

S=input("Enter the string =")
t=input("enter the tag =")

print('<'+t+'>'+S+'</'+t+'>')