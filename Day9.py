# 9. Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

a= int(input("Enter the first angle==>"))
b= int(input("Enter the Second angle==>"))
c= int(input("Enter the third angle==>"))

if a>0 and b>0 and c>0 and (a+b+c==180):
    print("It can form triangle")
else:
    print("It cannot form traingle")


