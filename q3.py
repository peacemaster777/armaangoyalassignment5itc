#ques3
#import module
import math

def calculate_triangle_area(a, b, c):
    # Check if the combination of sides is possible
    if a + b > c and b + c > a and c + a > b:
        # semi-perimeter
        s = (a + b + c) / 2
        #  area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return "The combination of sides is not possible."

# Example usage
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

area = calculate_triangle_area(side1, side2, side3)
print("The area of the triangle is:", area)

    


