# Assignment 3:

# 1.Write a program to demonstrate all arithmetic operators using two user-defined numbers.

# Program:
a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Exponent:", round(a ** b, 5))
if b==0:
    print ("Divisor should not be zero")
    print("Try another number to perform modulus, Division and Floor Division")
else:
    print("Modulus:", a % b)
    print("Division:", a / b)
    print("Floor Division:", a // b)

'''Output:
Enter first number: 5.5
Enter second number: 2.5
Addition: 8.0
Subtraction: 3.0
Multiplication: 13.75
Exponent: 70.94254
Modulus: 0.5
Division: 2.2
Floor Division: 2.0'''


# 2.Write a program to compare two numbers using relational operators and display the result.

# Program:
a = int(input("Enter a value : "))
b = int(input("Enter b value: "))
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

'''Output:
Enter a value : 4
Enter b value: 4
a == b: True
a != b: False
a > b: False
a < b: False
a >= b: True
a <= b: True'''


# 3.Explain logical operators (and, or, not) with a truth table and a sample program.
'''
Truth Table:
____________________________________________
| A     | B     | A and B | A or B | not A |
| ----- | ----- | ------- | ------ | ----- |
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |

Program:'''
a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

'''Output:
a and b: False
a or b: True
not a: False'''


# 4.Write a program to check whether a number lies between 10 and 50 using logical operators.

# Program:
num = int(input("Enter a number: "))
if num >= 10 and num <= 50:
    print("Number is between 10 and 50")
else:
    print("Number is NOT between 10 and 50")

'''Output:
Enter a number: 25
Number is between 10 and 50'''


# 5.Demonstrate the use of assignment operators (=, +=, -=, *=, /=) with examples.

# Program:
x = 10
print("Initial value:", x)
x += 5
print("After += :", x)
x -= 3
print("After -= :", x)
x *= 2
print("After *= :", x)
x /= 4
print("After /= :", x)

'''Output:
Initial value: 10
After += : 15
After -= : 12
After *= : 24
After /= : 6.0
'''

# 6.Write a program to check whether a given value exists in a list using membership operators.

# Program:
lst = [10, 20, 30, 40, 50]
value = int(input("Enter value to search: "))
if value in lst:
    print("Value exists in list")
else:
    print("Value does not exist in list")

'''Output:
Enter value to search: 30
Value exists in list'''


''' 7.What is the difference between == and is operators? Write a program to prove it.

== -> checks value equality (are the contents the same)
is -> checks identity, compares memory locations (are they the same object in memory)

Program:'''
# Same values, different objects
a = [1, 2, 3]
b = [1, 2, 3]
print("a == b:", a == b)  # True (values are equal)
print("a is b:", a is b)  # False (different memory locations)

# Same object
c = a
print("a == c:", a == c)  # True
print("a is c:", a is c)  # True (same object)

# Small integers (special case: storing Cache )
x = 10
y = 10
print("x == y:", x == y)  # True
print("x is y:", x is y)  # True (Python reuses memory)

'''Output:
a == b: True
a is b: False
a == c: True
a is c: True
x == y: True
x is y: True
'''

# 8.Write a program to check whether a number is even or odd using operators.

# Program:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num,"is Even number")
else:
    print(num,"is Odd number")

'''Output:
Enter a number: 6
6 is Even number
'''

# 9.Write a program to calculate the area of a rectangle using arithmetic operators and user input.

# Program:
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle:", area)

'''Output:
Enter length: 6
Enter breadth: 4
Area of rectangle: 24.0'''


'''10.Explain operator precedence in Python and write a program showing how precedence affects the result.

Operator precedence determines which operation is performed first.

Order is high to low:
1. () (parentheses)
2. ** (exponent)
3. *, /, //, % (These are evaluated from left to right)
4. +, -
5. Comparison operators (==, !=, etc.)
6. Logical operators (and, or, not)

Program:'''
res = 10 + 5 * 2
result = (10 + 5) * 2
print("Without parentheses:", res)
print("With parentheses:", result)

'''Output:
Without parentheses: 20
With parentheses: 30
'''