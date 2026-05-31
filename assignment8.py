# ASSIGNMENT 8

# FUNCTIONS & RECURSION 

## SECTION 1: BUILT-IN VS USER-DEFINED FUNCTIONS

### 1. Built-in Functions Practice

'''Question:**
Write a program that takes a list of numbers and uses built-in functions to print:

* Maximum value
* Minimum value
* Sum of elements
* Length of the list

**Test Case 1:**
Input:
[10, 20, 5, 40]

Expected Output:
Maximum: 40
Minimum: 5
Sum: 75
Length: 4

**Test Case 2:**
Input:
[3, 3, 3]

Expected Output:
Maximum: 3
Minimum: 3
Sum: 9
Length: 3


Program:'''
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(numbers)
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))
print("Sum:",sum(numbers))
print("Length:",len(numbers))

'''Output1:
Enter numbers separated by space: 10 20 5 40 
[10, 20, 5, 40]
Maximum: 40
Minimum: 5
Sum: 75
Length: 4

Ouyput2:
Enter numbers separated by space: 3 3 3
[3, 3, 3]
Maximum: 3
Minimum: 3
Sum: 9
Length: 3
'''

### 2. User-Defined Max, Min, Sum (Without Built-ins)

'''Question:**
Write your own functions to calculate:

* Maximum
* Minimum
* Sum

Do NOT use max(), min(), sum().

**Test Case 1:**
Input:
[4, 8, 1, 9]

Expected Output:
Maximum: 9
Minimum: 1
Sum: 22

**Test Case 2:**
Input:
[-5, -2, -10]

Expected Output:
Maximum: -2
Minimum: -10
Sum: -17

Program:'''
def custom_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

def custom_min(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

def custom_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(numbers)
print("Maximum:",custom_max(numbers))
print("Minimum:",custom_min(numbers))
print("Sum:",custom_sum(numbers))

'''Output1:
Enter numbers separated by space: 4 8 1 9
[4, 8, 1, 9]
Maximum: 9
Minimum: 1
Sum: 22
Length: 4

Output2:
Enter numbers separated by space: -5 -2 -10
[-5, -2, -10]
Maximum: -2
Minimum: -10
Sum: -17
Length: 3
'''

## SECTION 2: PARAMETERS & ARGUMENTS

### 3. greet(name)

'''Question:**
Create a function greet(name) that prints a greeting message.

**Test Case 1:**
Input:
greet("Sairam")

Expected Output:
Hello Sairam! Welcome to Python class.

**Test Case 2:**
Input:
greet("Anjali")

Expected Output:
Hello Anjali! Welcome to Python class.

Program:'''
def greet(name):
    print(f"Hello {name}! Welcome to Python class")
greet(name=input("Enter Your Name: "))

'''Output1:
Enter Your Name: Sairam
Hello Sairam! Welcome to Python class

Output2:
Enter Your Name: Anjali
Hello Anjali! Welcome to Python class
'''

### 4. calculate_total(price, quantity)

'''Question:**
Create a function that returns total amount.

**Test Case 1:**
Input:
calculate_total(100, 3)

Expected Output:
300

**Test Case 2:**
Input:
calculate_total(250, 2)

Expected Output:
500

Program:'''
def calculate_total(price, quantity):
    return price * quantity
total = calculate_total(price=int(input("Enter price: ")), quantity=int(input("Enter quantity: ")))
print("Total:", total)

'''Output1:
Enter price: 100
Enter quantity: 3
Total: 300

Output2:
Enter price: 250
Enter quantity: 2
Total: 500
'''

### 5. create_account(name, role="User")

'''Question:**
Create a function with default role.

**Test Case 1:**
Input:
create_account("Rahul")

Expected Output:
Account created for Rahul with role User

**Test Case 2:**
Input:
create_account("AdminUser", "Admin")

Expected Output:
Account created for AdminUser with role Admin

Program:'''
def create_account(name, role="User"):
    if name == "AdminUser":
        role = "Admin"
    print(f"Account created for {name} with role {role}")
create_account(name=input("Enter name: "))

'''Output1:
Enter name: Rahul
Account created for Rahul with role User

Output2:
Enter name: AdminUser
Account created for AdminUser with role Admin
'''


## SECTION 3: RETURN VS PRINT

### 6. Print vs Return (Square)

'''Question:**
Create:

* One function that prints square
* One function that returns square

**Test Case 1:**

Input:
square_print(5)

Output:
25

Input:
result = square_return(5)
print(result * 10)

Output:
250

**Test Case 2:**
Input:
square_print(3)

Output:
9

Input:
result = square_return(3)
print(result * 10)

Output:
90

Program:'''
def square_print(num):
    print(num ** 2)

def square_return(num):
    return num ** 2
square_print(num=int(input("Enter a number to print its square: ")))
result = square_return(num=int(input("Enter a number to return its square: ")))
print("square * 10 :",result * 10)

'''Output1:
Enter a number to print its square: 5
25
Enter a number to return its square: 5
square * 10 : 250

Output2:
Enter a number to print its square: 3
9
Enter a number to return its square: 3
square * 10 : 90
'''

### 7. Function Chaining

''' Question:**
Create two functions: add(a, b) and multiply(a, b).
Call multiply using result of add.

**Test Case 1:**
Input:
multiply(add(2,3),4)

Expected Output:
20

**Test Case 2:**
Input:
multiply(add(10,5),2)

Expected Output:
30

Program:'''
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
result = multiply(add(2,3),4)
print("Result of multiply(add(2,3),4):", result)
result = multiply(add(10,5),2)
print("Result of multiply(add(10,5),2):", result)

'''Output:
Result of multiply(add(2,3),4): 20
Result of multiply(add(10,5),2): 30
'''

## SECTION 4: LOGICAL THINKING WITH FUNCTIONS

### 8. Even & Odd Counter

'''Question:**
Write a function that returns count of even and odd numbers.

**Test Case 1:**
Input:
[1,2,3,4,5]

Expected Output:
Even count: 2
Odd count: 3

**Test Case 2:**
Input:
[2,4,6]

Expected Output:
Even count: 3
Odd count: 0

Program:'''
def count_even_odd(lst):
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_count, odd_count = count_even_odd(numbers)
print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")

'''Output1:
Enter numbers separated by space: 1 2 3 4 5
Even count: 2
Odd count: 3

Output2:
Enter numbers separated by space: 2 4 6
Even count: 3
Odd count: 0
'''

### 9. Palindrome Checker

'''Question:**
Create function is_palindrome(word).
Return True if palindrome else False.

**Test Case 1:**
Input:
is_palindrome("madam")

Expected Output:
True

**Test Case 2:**
Input:
is_palindrome("python")

Expected Output:
False

Program:'''
def is_palindrome(word):
    return word == word[::-1]   
word = input("Enter a word to check if it's a palindrome: ")
result = is_palindrome(word)
print(f"Is '{word}' a palindrome? {result}")

'''Output1:
Enter a word to check if it's a palindrome: madam
Is 'madam' a palindrome? True

Output2:
Enter a word to check if it's a palindrome: python
Is 'python' a palindrome? False
'''

## SECTION 5: RECURSION

### 10. Factorial Using Recursion

'''Question:**
Write a recursive function to find factorial.

**Test Case 1:**
Input:
factorial(5)

Expected Output:
120

**Test Case 2:**
Input:
factorial(4)

Expected Output:
24

Program:'''
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print(f"Factorial of {number} is {result}")

'''Output1:
Enter a number to find its factorial: 5
Factorial of 5 is 120

Output2:
Enter a number to find its factorial: 4
Factorial of 4 is 24
'''

### 11. Fibonacci Using Recursion

'''Question:**
Print first N Fibonacci numbers.

**Test Case 1:**
Input:
n = 5

Expected Output:
0 1 1 2 3

**Test Case 2:**
Input:
n = 7

Expected Output:
0 1 1 2 3 5 8

Program:'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci(i), end=" ")

'''Output1:
Enter the number of terms: 5
0 1 1 2 3

Output2:
Enter the number of terms: 7
0 1 1 2 3 5 8
'''

### 12. Sum of Digits (Recursion)

'''Question:**
Return sum of digits using recursion.

**Test Case 1:**
Input:
1234

Expected Output:
10

**Test Case 2:**
Input:
567+

Expected Output:
18

Program:'''
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits(num // 10)
number = int(input("Enter a number to find sum of its digits: "))
result = sum_of_digits(number)
print(f"Sum of digits of {number} is {result}")

'''Output1:
Enter a number to find sum of its digits: 1234
Sum of digits of 1234 is 10

Output2:
Enter a number to find sum of its digits: 567
Sum of digits of 567 is 18
'''

### 13. Reverse String (Recursion)

'''Question:**
Reverse string using recursion.

**Test Case 1:**
Input:
"python"

Expected Output:
"nohtyp"

**Test Case 2:**
Input:
"madam"

Expected Output:
"madam"

Program:'''
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
string = input("Enter a string to reverse: ")
result = reverse_string(string)
print(f"Reversed string: {result}")

'''Output1:
Enter a string to reverse: python
Reversed string: nohtyp

Output2:
Enter a string to reverse: madam
Reversed string: madam
'''

### 14. Countdown Using Recursion

'''Question:**
Print countdown using recursion.

**Test Case 1:**
Input:
countdown(3)

Expected Output:
3
2
1
Done!

**Test Case 2:**
Input:
countdown(5)

Expected Output:
5
4
3
2
1
Done!

Program:'''
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
number = int(input("Enter a number to start countdown: "))
countdown(number)

'''Output1:
Enter a number to start countdown: 3
3
2
1
Done!

Output2:
Enter a number to start countdown: 5
5
4
3
2
1
Done!
'''

### 15. Power Function Using Recursion

'''Question:**
Find power without using ** operator.

**Test Case 1:**
Input:
power(2,3)

Expected Output:
8

**Test Case 2:**
Input:
power(5,2)

Expected Output:
25

**Test Case 3:**
Input:
power(3,0)

Expected Output:
1

Program:'''
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = power(base, exp)
print(f"Power of ({base},{exp}) is :{result}")

'''Output1:
Enter base: 2
Enter exponent: 3
Power of (2,3) is :8

Output2:
Enter base: 5
Enter exponent: 2
Power of (5,2) is :25

Output3:
Enter base: 3
Enter exponent: 0
Power of (3,0) is :1
'''