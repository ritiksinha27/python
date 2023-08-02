#Write a Python program to remove repeated consecutive characters and replace them with single letters and print a updated string.
'''
def cons():
    S=input("Enter the string =")
    L=' '.join(x for x in S.split())
    print(L)
cons()'''

def test(text="Ritiik"):
  result = []
  for x in text:
    if not result or result[-1] != x:
      result.append(x)
  x= ''.join(result)
  print(x)

test()
