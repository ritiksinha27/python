#Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

S=input("Enter the string =")
print(S[-1] + S[1:len(S)-1:] + S[0])