print("python Developer")
# https://github.com/Shivardy006/my-project.git
a = input("Enter a value :")
student = ["sai","Ram","Shiva","Prasad","Pavan"]
print("Original list:", student)
# 1. append()
student.append("Kiran")
print("\nAfter append:", student)

# 2. copy()
student_copy = student.copy()
print("Copied list:", student_copy)

# 3. count()
count_ram = student.count("Ram")
print("Count of 'Ram':", count_ram)

# 4. extend()
student.extend(["Arjun", "Teja"])
print("After extend:", student)

# 5. index()
index_shiva = student.index("Shiva")
print("Index of 'Shiva':", index_shiva)

# 6. insert()
print(student[2]) 
student.insert(2, "Nani")
print("After insert at index 2:", student)

# 7. pop()
popped_item = student.pop()  # removes last element
print("Popped item:", popped_item)
print("After pop:", student)

# 8. remove()
student.remove("Ram")
print("After removing 'Ram':", student)

# 9. reverse()
student.reverse()
print("After reverse:", student)

# 10. sort()
student.sort()  # ascending order
print("After sort:", student)

# 11. clear()
temp_list = student.copy()
temp_list.clear()
print("After clear (on copy):", temp_list)