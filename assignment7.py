# Assignment 7:

'''
1.Write1.Write a program to take a string from the user and:

    a.Convert it to uppercase

    b.Convert it to lowercase  

Program:'''
text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

'''Output:
Enter a string: Shiva
Uppercase: SHIVA
Lowercase: shiva
'''

'''2.Write a program to count the number of vowels in a given string using string methods.

Program:'''
text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

'''Output:
Enter a string: Shiva
Number of vowels: 2
'''

'''3.Write a program to check whether a given string starts with a specific word using a string method.

Program:'''
text = input("Enter a string: ")
word = input("Enter the word to check: ")
if text.startswith(word):
    print("The string starts with :",word)
else:
    print("The string does not start with :",word)

'''Output:
Enter a string: Shiva Reddy
Enter the word to check: Shiva
The string starts with : Shiva
'''

'''4.Write a program to replace all spaces in a string with a hyphen (-).

Program:'''
text = input("Enter a string: ")
new_text = text.replace(" ", "-")
print("Modified string:", new_text)

'''Output:
Enter a string: Python Training
Modified string: Python-Training
'''

'''5.Write a program to find the length of a string without using the len() function
(Hint: use a string method).

Program:'''
text = input("Enter a string: ")
count = 0
for _ in text:
    count += 1
print("Length of the string:", count)

'''Output:
Enter a string: Shiva
Length of the string: 5
'''

'''6.Write a program to check whether a given string is a palindrome using string methods.

Program:'''
text = input("Enter a string: ")
if text == text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

'''Output:
Enter a string: 12321
The string is a palindrome
'''

'''7.Write a program to count the number of words in a sentence.

Program:'''
sentence = input("Enter a sentence: ")
words = sentence.split()  # splits by spaces
print("Number of words:", len(words))

'''Output:
Enter a sentence: Python training is easy
Number of words: 4
'''

'''8.Write a program to find how many times a particular character appears in a string.

Program:'''
text = input("Enter a string: ").lower()
char = input("Enter the character to count: ").lower()
count = text.count(char)
print("The character",char,"appears",count,"times")

'''Output:
Enter a string: AsSignment
Enter the character to count: s
The character s appears 2 times
'''

'''9.Write a program to remove leading and trailing spaces from a string.

Program:'''
text = input("Enter a string with extra spaces: ")
clean_text = text.strip()
print("String after removing spaces:", clean_text)

'''Output:
Enter a string with extra spaces:     Python
String after removing spaces: Python
'''

'''10.Write a program to check whether a string contains only digits using string methods.

Program:'''
text = input("Enter a string: ")
if text.isdigit():
    print("The string contains only digits")
else:
    print("The string does not contain only digits")

'''Output:
Enter a string: Shiva123
The string does not contain only digits
'''