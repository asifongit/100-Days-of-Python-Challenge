# 11. Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

# I need to find a Simple Interest
# i have principle(p) , Rate(r) and Time(t)
# Formula is SimpleInterest= p*r*t all of this divide by 100


def find_Simple_Interest(principal, Rate, Time):
    SimpleInterest=(principal*Rate*Time)/100
    return f"SimpleInterest is {SimpleInterest}"



p= float(input("Enter the principal value =>"))
r= float(input("Enter the Rate =>"))
t= float(input("Enter the Time =>"))

result=find_Simple_Interest(p,r,t)
print(result)
