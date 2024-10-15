#Get input from user for width and length
width = float(input("Enter the width of a rectangle: "))
length = float(input("Enter the length of the rectangle: "))

#Perform calculation for Area and Perimeter
Area = width * length
Perimeter = 2 * (width + length)

#print the result
print(f"The area of the rectangle is {Area} and the perimenter of the rectangle is {Perimeter}")