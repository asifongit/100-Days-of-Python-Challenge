# Write a program that will tell whether the given number is divisible by 3 & 6.

a= int(input("Enter the number: "))

if (a%3==0 and a%6==0):
    print("Number is divisible by both 3 and 6")
else:
    print("Number is NOT divisible by both 3 and 6")