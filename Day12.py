# 12. Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

#formula of voumen of cylinder is π*r2*h

def find_volume(radius, height):
    pi = 3.14159
    volume = pi * radius * radius * height
    return volume


radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

volume = find_volume(radius, height)

# Convert cubic centimeters to litres
litres = volume / 1000

# Cost of milk
cost_of_milk = litres * 40

print(f"Volume of Cylinder: {volume:.2f} cm³")
print(f"Milk Capacity: {litres:.2f} litres")
print(f"Cost of Milk: Rs. {cost_of_milk:.2f}")