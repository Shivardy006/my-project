# Assignment 2:

'''1.Create a list of 5 student names and:

    a)Add one more name

    b)Remove one name

    c)Display the final list'''

# Program:
# Step 1: Create a list of 5 student names
students = ["Shiva", "Narsimha", "Pavan", "Uday", "Srinadh"]
print("Original List is :", students)
# Step 2: Add one more name
students.append("Rocky")
print("Added List is :", students)
# Step 3: Remove one name
students.remove("Rocky")
# Step 4: Display the final list
print("Final list of students:", students)

'''Output:
Original List is : ['Shiva', 'Narsimha', 'Pavan', 'Uday', 'Srinadh']
Added List is : ['Shiva', 'Narsimha', 'Pavan', 'Uday', 'Srinadh', 'Rocky']
Final list of students: ['Shiva', 'Narsimha', 'Pavan', 'Uday', 'Srinadh']
'''


# 2.Write a program to find the largest and smallest elements in a list without using built-in functions.

# Program:
# create a list of numbers
numbers = [12, 45, 2, 67, 34, 9, 1]
# Initialize largest and smallest with the first element of the list
largest = numbers[0]
smallest = numbers[0]
# Loop through the list to find largest and smallest
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest element:", largest)
print("Smallest element:", smallest)

'''Output:
Largest element: 67
Smallest element: 1
'''


'''3.Create a tuple with mixed data types and:

    a)Access elements using indexing

    b)Explain why tuples are immutable

    c)Convert a tuple into a list, modify an element, and convert it back into a tuple.'''

# Program:
# Tuple with mixed data types
my_tuple = (10, "Sai", 3.14, True)
# (a) Accessing elements
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])
print("Third element:", my_tuple[2])
print("fourth element:", my_tuple[3])
print("Last element:", my_tuple[-1])
# (c) Convert tuple to list
temp_list = list(my_tuple)
# Modify an element
temp_list[1] = "Ram"
# Convert back to tuple
my_tuple1 = tuple(temp_list)
# Display modified tuple
print("Modified tuple:", my_tuple1)
# (b) Trying to modify a tuple element (will cause an error)
my_tuple[1] = "Ram"  # this line will raise TypeError

'''Output:
First element: 10
Second element: Sai
Third element: 3.14
fourth element: True
Last element: True
Modified tuple: (10, 'Ram', 3.14, True)
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 18, in <module>
TypeError: 'tuple' object does not support item assignment
'''


# 4.Write a program to remove duplicate values from a list using a set.

# Program:
# Input list with duplicates
my_list = [1, 2, 3, 4, 1, 5, 3]
# Remove duplicates using set
unique_set = set(my_list)
# Convert back to list (optional, if you want a list)
unique_list = list(unique_set)
# Display the results
print("Original list:", my_list)
print("List after removing duplicates:", unique_list)

'''Output:
Original list: [1, 2, 3, 2, 4, 1, 5, 3]
List after removing duplicates: [1, 2, 3, 4, 5]
'''


'''5.Create a dictionary with employee details (id, name, salary).
Perform:

    a)Add a new key

    b)Update salary
    
    c)Delete a key'''

# Program:
# Employee dictionary
employee = {
    "id": 7,
    "name": "Sairam",
    "salary": 35000
}
print("Original employee details:", employee)
# Add a new key: department
employee["department"] = "HR"
print("After adding department:", employee)
# Update salary
employee["salary"] = 850000
print("After updating salary:", employee)
# Delete the department key
del employee["department"]
print("After deleting department:", employee)

'''Output:
Original employee details: {'id': 7, 'name': 'Sairam', 'salary': 35000}
After adding department: {'id': 7, 'name': 'Sairam', 'salary': 35000, 'department': 'HR'}
After updating salary: {'id': 7, 'name': 'Sairam', 'salary': 850000, 'department': 'HR'}
After deleting department: {'id': 7, 'name': 'Sairam', 'salary': 850000}
'''


# 6.Write a program to iterate through a dictionary and print: Keys, Values ,Key-value pairs.

# Program:
# Sample dictionary
employee = {
    "id": 7,
    "name": "Sairam",
    "salary": 85000
}
# Print keys
print("Keys:")
for key in employee:
    print(key)
# Print values
print("\nValues:")
for value in employee.values():
    print(value)
# Print key-value pairs
print("\nKey-Value Pairs:")
for key, value in employee.items():
    print(key, ":", value)

'''Output:
Keys:
id
name
salary

Values:
7
Sairam
85000

Key-Value Pairs:
id : 7
name : Sairam
salary : 85000'''


# 7.Declare two sets, perform and display: Union, Intersection, Difference.

# Program1:
# Declare two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Union
union_set = set1 | set2
print("Union:", union_set)
# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)
# Difference (elements in set1 but not in set2)
difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)

# Program2:
# Declare two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Union
union_set = set1.union(set2)
print("Union:", union_set)
# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)
# Difference (elements in set1 but not in set2)
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

'''Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Difference (set1 - set2): {1, 2, 3}
'''

# 8.Write a program to count the frequency of each element in a list using a dictionary.

# Program1:
# list
my_list = [1,2,1,3,2,3,2,5,4]
# Create an empty dictionary to store frequencies
frequency = {}
# Loop through the list and count occurrences
for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
# Display the frequency of each element
print("Frequency of each element:")
for key, value in frequency.items():
    print(key, ":", value)

# Program2:
my_list = [1,2,1,3,2,3,2,5,4]
frequency = {}
for item in my_list:
    # get() returns the current count if exists, else 0
    frequency[item] = frequency.get(item, 0) + 1
print("Frequency using dict.get():", frequency)


'''Output1:
Frequency of each element:
1 : 2
2 : 3
3 : 2
4 : 1
5 : 1

Output2:
Frequency using dict.get(): {1: 2, 2: 3, 3: 2, 4: 1, 5: 1}
'''

'''9.Explain the difference between list, tuple, set, and dictionary with one real-time example each.

Ans:
1. List
Ordered: Elements are stored in the order you insert them.
Mutable: You can add, remove, or change elements.
Allows duplicates.
Real-time example: Shopping cart items
shopping_cart = ["mango", "bread", "apples", "butter"]
You can add or remove items (shopping_cart.append("bread"))
Duplicates make sense (buying 2 apples).

2. Tuple
Ordered: Elements are in a fixed order.
Immutable: Cannot be changed after creation.
Allows duplicates.
Real-time example: GPS coordinates
location = (40.7128, -74.0060)  # (latitude, longitude)
Coordinates shouldn’t change (immutable).
Order matters (latitude first, longitude second).

3. Set
Unordered: No specific order of elements.
Mutable: You can add or remove elements.
No duplicates allowed.
Real-time example: Unique users visiting a website
unique_visitors = {"Sairam", "Shiva", "uday"}
Adding "Shiva" again has no effect.
Order is irrelevant; we only care about uniqueness.

4. Dictionary
Key-value pairs: Each key maps to a value.
Mutable: Can add, update, or remove entries.
Keys are unique, values can repeat.
Real-time example: Student details
student = {"id": 1, "name": "Shiva", "grade": "A+"}
You can quickly access data by key (student["name"])
Keys must be unique ("id" can appear only once).

Comparision Table:
___________________________________________________________________________________
| Data Type  | Ordered | Mutable | Duplicates | Example                           |
| ---------- | ------- | ------- | ---------- | --------------------------------- |
| List       | Yes     | Yes     | Yes        | Shopping cart items               |
| Tuple      | Yes     | No      | Yes        | GPS coordinates                   |
| Set        | No      | Yes     | No         | Unique website visitors           |
| Dictionary | No      | Yes     | Keys: No   | Student details (id, name, grade) |
'''