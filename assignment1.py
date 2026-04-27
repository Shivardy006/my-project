# Assignment 1:

# 1. Program to Calculate the Area of a Circle:

# Program:
import math
#Input Radius
radius = float(input("Enter the radius of the circle: "))
# Area of circle
area = math.pi * radius ** 2
print("The area of the circle is:", round(area, 5))

'''Output:
Enter the radius of the circle: 10
The area of the circle is: 314.15927
'''

# 2. Program to Calculate Total Cost After Discount

# Program:
#Input:
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))
# Discount amount
discount_amount = (discount_percentage / 100) * original_price
# total cost after discount
total_cost = original_price - discount_amount
print("The total cost after discount is:", total_cost)

'''Output:
Enter the original price: 1000
Enter the discount percentage: 20
The total cost after discount is: 800.0
'''

# 3. Program to Calculate Simple Interest

# Program:
# Input: 
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time in years: "))
# Simple interest
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)


'''Output:
Enter the principal amount: 2000
Enter the rate of interest (in %): 6
Enter the time in years: 3
The simple interest is: 360.0
'''

# 4. Program to Calculate Total Salary

# Program:
# Input:
basic_salary = float(input("Enter the basic salary: "))
HRA = float(input("Enter the HRA: "))
DA = float(input("Enter the DA: "))
# Total salary
total_salary = basic_salary + HRA + DA
print("The total salary is:", total_salary)

'''Output:
Enter the basic salary: 30000
Enter the HRA: 7000
Enter the DA: 4000
The total salary is: 41000.0
'''

# 5. Program to Calculate Distance Traveled

# Program:
# Input:
speed = float(input("Enter the speed of the vehicle (km/h): "))
time = float(input("Enter the time traveled (hours): "))
# Calculate distance
distance = speed * time
print("The distance traveled is:", distance)

'''Output:
Enter the speed of the vehicle (km/h): 80
Enter the time traveled (hours): 1.5
The distance traveled is: 120.0
'''

# 6. Program to Convert Temperature from Celsius to Fahrenheit

# Program:
# Input:
celsius = float(input("Enter temperature in Celsius: "))
# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is:", fahrenheit)

'''Output:
Enter temperature in Celsius: 25
The temperature in Fahrenheit is: 77.0
'''

# 7. Program to Find the Maximum of Two Numbers Using Ternary Operator

# Program:
# Input:
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
# Find maximum using ternary operator
maximum = a if a > b else b
print("The maximum of the two numbers is:", maximum)

'''Output:
Enter the first number: 35
Enter the second number: 20
The maximum of the two numbers is: 35.0
'''

# 8. Swap Two Numbers

# Program1:
# Input:
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
# Swap without third variable using arithmetic
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, ", b =", b)

# Program2:
# Input:
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
# Swap using tuple unpacking
a, b = b, a
print("After swapping: a =", a, ", b =", b)

'''Output:
Enter the first number (a): 15
Enter the second number (b): 20
After swapping: a = 20.0 , b = 15.0
'''

# 9. Next Multiple of 100

# Program:
# Input:
n = int(input("Enter a number: "))
# Calculate next multiple of 100
next_multiple = ((n // 100) + 1) * 100
print("The next multiple of 100 is:", next_multiple)

'''Output:
Enter a number: 320
The next multiple of 100 is: 400
'''

# 10. Splitting into the Teams
 
# Program:
# Input:
people = int(input("Enter the number of people: "))
# Calculate number of teams and leftover people
teams = people // 2
leftover = people % 2
print("Teams =", teams, ", Leftover =", leftover)

'''Output:
Enter the number of people: 7
Teams = 3 , Leftover = 1
'''