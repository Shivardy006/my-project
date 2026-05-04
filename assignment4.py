# Assignment 4:
'''
Conditional statements:

1.Write a program to check whether a given number is positive, negative, or zero.

Program:'''
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

'''Output:
Enter a number: 4
The number is positive
'''

# 2.Write a program to check whether a given number is even or odd using an if-else statement.

# Program:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num,"is even")
else:
    print(num,"is odd")

'''Output:
Enter a number: 8
8 is even
'''

# 3.Write a program to find the largest of two numbers entered by the user.

# Program:
a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
if a > b:
    print("The largest number is", a)
else:
    print("The largest number is", b)

'''Output:
Enter a value: 6
Enter b value: 4
The largest number is 6.0'''


# 4.Write a program to find the largest of three numbers using if-elif-else.

# Program:
a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
c = float(input("Enter c value: "))
if a >= b and a >= c:
    print("The largest number is", a)
elif b >= a and b >= c:
    print("The largest number is", b)
else:
    print("The largest number is", c)

'''Output:
Enter a value: 8
Enter b value: 5
Enter c value: 9
The largest number is 9.0'''


# 5.Write a program to check whether a given year is a leap year or not.

# Program:
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

'''Output:
Enter a year: 2024
2024 is a leap year
'''

# 6.Write a program to check whether a person is eligible to vote based on age input.

# Program:
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

'''Output:
Enter your age: 16
You are not eligible to vote.
'''

''' 7.Write a program to display student grade based on the following conditions:

    Marks ≥ 90 → Grade A

    Marks ≥ 75 → Grade B

    Marks ≥ 60 → Grade C

    Marks < 60 → Grade D

Program:'''
marks = float(input("Enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"
print("Your grade is", grade)

'''Output:
Enter your marks: 96
Your grade is A
'''

# 8.Write a program to check whether a given character is: a vowel or a consonant

# Program:
char = input("Enter a single character: ").lower()
if char in 'aeiou':
    print("The character is a vowel")
else:
    print("The character is a consonant")

'''Output:
Enter a single character: i
The character is a vowel
'''

'''9.Write a program to create a simple calculator using if- elif -else
(addition, subtraction, multiplication, division).

Program:'''
a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    print("Result:", a + b)
elif operation == '-':
    print("Result:", a - b)
elif operation == '*':
    print("Result:", a * b)
elif operation == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operation.")

'''Output:
Enter first number: 4
Enter second number: 0
Enter operation (+, -, *, /): /
ERROR!
Error: Division by zero!
'''

# 10.Write a program to check whether a given number is a three-digit number or not using conditional statements.
 
# Program:
num = int(input("Enter an integer value: "))
if 100 <= abs(num) <= 999:     # abs()->negative numbers are handled correctly
    print(num,"is a three-digit number")
else:
    print(num,"is not a three-digit number")

'''Output:
Enter an integer value: -565
-565 is a three-digit number
'''