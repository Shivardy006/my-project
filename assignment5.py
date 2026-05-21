#Assignment 5:

'''1.Write a program to print numbers from 1 to N using a loop.
(N is given by the user)

Program:'''
N=int(input("Enter N value: "))
for i in range(1,N+1):
   print(i)

'''Output:
Enter N value: 4
1
2
3
4
'''

'''2.Write a program to find the sum of all even numbers between 1 and N using a loop.

Program:'''
N=int(input("Enter N value: "))
sum=0
for i in range(2,N+1):
   if i%2==0:
       sum += i
print("sum of",N,"even numbers is:",sum)

'''Output:
Enter N value: 8
sum of 8 even numbers is: 20
'''

'''3.Write a program to reverse a given number using a loop.
Example: Input → 1234, Output → 4321

Program:'''
N=int(input("Enter a Number series:"))
reversed_num = 0
temp = N
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10 
print("Reversed number is:", reversed_num)

'''Output:
Enter a Number series:1234
Reversed number is: 4321
'''

'''4.Write a program to count the number of digits in a given number using a loop.

Program:'''
num = int(input("Enter a number: "))
count = 0
temp = num

while temp > 0:
    count += 1
    temp //= 10

print("Number of digits:", count)

'''Output:
Enter a number: 12233
Number of digits: 5
'''

'''5.Write a program to generate the multiplication table of a given number up to 10.
expected
 
output expected : 
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
.
.
.
5 * 10 = 50

Program:'''
N = int(input("Enter a number: "))
for i in range(1,11):
    print( N,"*",i,"=",N*i)

'''Output:
Enter a number: 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
'''

'''6.Write a program to print a square pattern of stars of size N:

****
****       
****
****

and 

* * * *
* * * *       
* * * *
* * * *
Program 1:'''
N = int(input("Enter the size of the square: "))
for i in range(N):
    for j in range(N):
        print("*",end="")
    print()

'''Output:
Enter the size of the square: 4
****
****
****
****

Program 2:'''
N = int(input("Enter the size of the square: "))
for i in range(N):
    for j in range(N):
        print("*",end=" ")
    print()

'''Output:
Enter the size of the square: 4
* * * * 
* * * * 
* * * * 
* * * * 
'''

'''7.Write a python program to print a complete diamond shape using stars (*) with nested loops.

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

Program:'''
N = int(input("Enter the number of rows for the diamond (odd number): "))
# Upper part
for i in range(1, N+1, 2):
    print(" " * ((N-i)//2) + "*" * i)
# Lower part
for i in range(N-2, 0, -2):
    print(" " * ((N-i)//2) + "*" * i)

'''Output:
Enter the number of rows for the diamond (odd number): 9
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

'''8.Write a python program to display this table using nested loops.


1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15
16 17 18 19 20

Program:'''
rows = 4
cols = 5
num = 1
for i in range(rows):
    for j in range(cols):
        print(num, end=" ")
        num += 1
    print()

'''Output:
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
'''