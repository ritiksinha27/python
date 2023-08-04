# Write a Python program to split a list based on the first character of a word.

# def spl():
#     L=[x for x in input("Enter the List =").split(',')]
#     d={}
#     for i in L:
#         if i[0] in d.keys():
#             d[i[0]]+=(' , '+i)
#         else:
#             d[i[0]]=(i)
#     print(d)
# spl()

def spl():
    from itertools import groupby
    from operator import itemgetter

    word_list = ['be','have','do','say' ,'get','make','go','know','take','see','come','think',
         'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

    for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
        print(letter)
        for word in words:
            print(word)
spl()
doubt