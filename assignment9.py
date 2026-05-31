# ASSIGNMENT 9

# LAMBDA & HIGHER-ORDER FUNCTIONS ASSIGNMENT

## SECTION 1: LAMBDA FUNCTIONS

### 1. Basic Lambda Function
'''Question:**
Create a lambda function to find the square of a number.

**Test Case 1:**
Input:
square = lambda x: x * x
square(5)

Expected Output:
25

**Test Case 2:**
square(8)

Expected Output:
64

Program:'''
def square(x):
    return lambda x: x * x
print(square(5))
print(square(8))

'''Output:
25
64
'''

### 2. Lambda with Multiple Arguments

'''Question:**
Create a lambda function to calculate the total price (price × quantity).

**Test Case 1:**
Input:
total = lambda price, qty: price * qty
total(100, 3)

Expected Output:
300

**Test Case 2:**
total(250, 2)

Expected Output:
500

Program:'''
def total(price, qty):
    return lambda price, qty: price * qty
print(total(100, 3))
print(total(250, 2))

'''Output:
300
500
'''

### 3. Lambda with Conditional Expression
'''Question:**
Create a lambda function that checks whether a number is even or odd.

**Test Case 1:**
Input:
check = lambda x: "Even" if x % 2 == 0 else "Odd"
check(10)

Expected Output:
Even

**Test Case 2:**
check(7)

Expected Output:
Odd

Program:'''
def check_odd_even(x):
    return lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_odd_even(10))
print(check_odd_even(7))

'''Output:
Even
Odd
'''

## SECTION 2: HIGHER-ORDER FUNCTIONS

# (A higher-order function is a function that takes another function as an argument.)

### 4. Function as Argument

'''Question:**
Create a function apply_operation(func, a, b)
It should take a function and two numbers.

**Test Case 1:**
Input:
apply_operation(lambda x, y: x + y, 5, 3)

Expected Output:
8

**Test Case 2:**
apply_operation(lambda x, y: x * y, 4, 6)

Expected Output:
24

Program:'''
def apply_operation(func, a, b):
    return func(a, b)
print(apply_operation(lambda x, y: x + y, 5, 3))
print(apply_operation(lambda x, y: x * y, 4, 6))

'''Output:
8
24
'''

### 5. Returning a Function

'''Question:**
Create a function multiplier(n) that returns a function to multiply any number by n.

**Test Case 1:**
Input:
double = multiplier(2)
double(5)

Expected Output:
10

**Test Case 2:**
triple = multiplier(3)
triple(4)

Expected Output:
12

Program:'''
def multiplier(n):
    return lambda x: x * n
double = multiplier(2)
print(double(5))
triple = multiplier(3)
print(triple(4))

'''Output:
10
12
'''

## SECTION 3: map()

### 6. Square All Numbers Using map()

'''Question:**
Given a list of numbers, use map() to return a list of squares.

**Test Case 1:**
Input:
[1, 2, 3, 4]

Expected Output:
[1, 4, 9, 16]

**Test Case 2:**
Input:
[5, 6, 7]

Expected Output:
[25, 36, 49]

Program:'''
numbers = map(int,input("Enter numbers seperated by space: ").split())
def square_all_numbers(numbers):
    return list(map(lambda x: x * x, numbers))
print(square_all_numbers(numbers))

'''Output:
Enter numbers seperated by space: 1 2 3 4
[1, 4, 9, 16]
Enter numbers seperated by space: 5 6 7
[25, 36, 49]
'''

### 7. Convert Strings to Uppercase Using map()

'''Question:**
Convert a list of names to uppercase using map().

**Test Case 1:**
Input:
["sairam", "anjali", "rahul"]

Expected Output:
["SAIRAM", "ANJALI", "RAHUL"]

**Test Case 2:**
Input:
["python", "django"]

Expected Output:
["PYTHON", "DJANGO"]

Program:'''
names = input("Enter names seperated by space: ").split()
def convert_to_uppercase(names):
    return list(map(lambda x: x.upper(), names))
print(convert_to_uppercase(names))

'''Output:
Enter names seperated by space: sairam anjali rahul
['SAIRAM', 'ANJALI', 'RAHUL']
Enter names seperated by space: python django
['PYTHON', 'DJANGO']
'''

## SECTION 4: filter()

### 8. Filter Even Numbers

'''Question:**
Use filter() to extract even numbers from a list.

**Test Case 1:**
Input:
[1,2,3,4,5,6]

Expected Output:
[2,4,6]

**Test Case 2:**
Input:
[10,15,20,25]

Expected Output:
[10,20]

Program:'''
numbers = map(int,input("Enter numbers seperated by space: ").split())
def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))
print(filter_even_numbers(numbers))

'''Output:
Enter numbers seperated by space: 1 2 3 4 5 6
[2, 4, 6]
Enter numbers seperated by space: 10 15 20 25
[10, 20]
'''

### 9. Filter Students with Passing Marks

'''Question:**
Given a list of marks, filter students who scored 50 or above.

**Test Case 1:**
Input:
[45, 67, 80, 30, 55]

Expected Output:
[67, 80, 55]

**Test Case 2:**
Input:
[90, 40, 49, 75]

Expected Output:
[90, 75]

Program:'''
marks = map(int,input("Enter marks seperated by space: ").split())
def filter_passing_students(marks):
    return list(filter(lambda x: x >= 50, marks))
print(filter_passing_students(marks))

'''Output:
Enter marks seperated by space: 45 67 80 30 55
[67, 80, 55]
Enter marks seperated by space: 90 40 49 75
[90, 75]
'''

## SECTION 5: reduce()

# (Note: Import reduce from functools)

### 10. Find Sum of List Using reduce()

'''Question:**
Use reduce() to find sum of elements.

**Test Case 1:**
Input:
[1,2,3,4]

Expected Output:
10

**Test Case 2:**
Input:
[5,5,5]

Expected Output:
15

Program:'''
from functools import reduce
numbers = map(int,input("Enter numbers seperated by space: ").split())
def find_sum(numbers):
    return reduce(lambda x, y: x + y, numbers)
print(find_sum(numbers))

'''Output:
Enter numbers seperated by space: 1 2 3 4
10
Enter numbers seperated by space: 5 5 5
15
'''

### 11. Find Product of List Using reduce()

'''Question:**
Use reduce() to find product of elements.

**Test Case 1:**
Input:
[1,2,3,4]

Expected Output:
24

**Test Case 2:**
Input:
[2,3,5]

Expected Output:
30

Program:'''
from functools import reduce
numbers = map(int,input("Enter numbers seperated by space: ").split())
def find_product(numbers):
    return reduce(lambda x, y: x * y, numbers)
print(find_product(numbers))

'''Output:
Enter numbers seperated by space: 1 2 3 4
24
Enter numbers seperated by space: 2 3 5
30
'''

## SECTION 6: PRACTICAL REAL-TIME EXAMPLES

### 12. Apply 10% Discount Using map()

'''Question:**
Given a list of prices, apply 10% discount to each price.

**Test Case 1:**
Input:
[100, 200, 300]

Expected Output:
[90.0, 180.0, 270.0]

**Test Case 2:**
Input:
[500, 1000]

Expected Output:
[450.0, 900.0]

Program:'''
prices = map(float,input("Enter prices seperated by space: ").split())
def apply_discount(prices):
    return list(map(lambda x: x * 0.9, prices))
print(apply_discount(prices))

'''Output:
Enter prices seperated by space: 100 200 300
[90.0, 180.0, 270.0]
Enter prices seperated by space: 500 1000
[450.0, 900.0]
'''

### 13. Filter High Salary Employees

'''Question:**
Given a list of salaries, filter salaries above 50,000.

**Test Case 1:**
Input:
[30000, 60000, 45000, 80000]

Expected Output:
[60000, 80000]

**Test Case 2:**
Input:
[55000, 40000, 75000]

Expected Output:
[55000, 75000]

Program:'''
salaries = map(int,input("Enter salaries seperated by space: ").split())
def filter_high_salary(salaries):
    return list(filter(lambda x: x > 50000, salaries))
print(filter_high_salary(salaries))

'''Output:
Enter salaries seperated by space: 30000 60000 45000 80000
[60000, 80000]
Enter salaries seperated by space: 55000 40000 75000
[55000, 75000]
'''

### 14. Calculate Total Bill Using reduce()

'''Question:**
Given a list of item prices in cart, calculate total bill.

**Test Case 1:**
Input:
[250, 150, 100]

Expected Output:
500

**Test Case 2:**
Input:
[999, 1]

Expected Output:
1000

Program:'''
from functools import reduce
prices = map(float,input("Enter item prices seperated by space: ").split())
def calculate_total_bill(prices):
    return reduce(lambda x, y: x + y, prices)
print(calculate_total_bill(prices))

'''Output:
Enter item prices seperated by space: 250 150 100
500
Enter item prices seperated by space: 999 1
1000
'''

### 15. Combined Example (map + filter)

'''Question:**
Given a list of numbers:

* First filter even numbers
* Then square them using map()

**Test Case 1:**
Input:
[1,2,3,4,5,6]

Expected Output:
[4,16,36]

**Test Case 2:**
Input:
[10,15,20]

Expected Output:
[100,400]

Program:'''
numbers = map(int,input("Enter numbers seperated by space: ").split())
def even_squares(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    squared_numbers = list(map(lambda x: x ** 2, even_numbers))
    return squared_numbers
print(even_squares(numbers))

'''Output:
Enter numbers seperated by space: 1 2 3 4 5 6
[4, 16, 36]
Enter numbers seperated by space: 10 15 20
[100, 400]
'''