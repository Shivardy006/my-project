#Assignment 6:

# 1. capitalize() – Capitalizes the first character of the string.
text = "shiva"
print(text.capitalize())           # "Shiva"
print("shiva".capitalize())        # "Shiva"
print("1shiva".capitalize())       # "1shiva"
print("SHIVA".capitalize())        # "Shiva"
print("shiva Reddy".capitalize())  # "Shiva reddy"


# 2. casefold() – Returns a lowercase version for caseless comparison.
print("Shiva".casefold())        # "shiva"
print("SHIVA".casefold())        # "shiva"
print("ShIvA".casefold())        # "shiva"
print("Shiva Reddy".casefold())  # "shiva reddy"
print("@SHIVA".casefold())       # "@shiva"


# 3. center(width, fillchar) – Centers the string with optional fill character.
print("Shiva".center(7))       # " Shiva "
print("ShIvA".center(7, "*"))  # "*ShIvA*"
print("Shiva".center(9, "-"))  # "--Shiva--"
print("Shiva".center(8, "-"))  # "-Shiva--"
print("Shiva".center(10))      # "  Shiva   "
print("123".center(5, "0"))    # "01230"


# 4. count(substring, start, end) – Counts occurrences of a substring.
text = "banana"
print(text.count("a"))          # 3
print(text.count("ba"))         # 1
print(text.count("na", 2))      # 2
print("Assisstance".count("s")) # 4
print("shiva shiva".count("i")) # 2


# 5. encode(encoding, errors) – Encodes string into bytes.
text = "Shiva"
print(text.encode())                            # b'Shiva'
print("shiva".encode("utf-8"))                  # b'shiva'
print("10/2".encode("utf-8"))                   # b'10/2'
print("safé".encode("ascii", errors="ignore"))  # b'saf'
print("safé".encode("ascii", errors="replace")) # b'saf?'


# 6. endswith(suffix, start, end) – Checks if string ends with a suffix.
text = "sample.py"
print(text.endswith(".py"))            # True
print(text.endswith("sample"))         # False
print("python".endswith("on"))         # True
print("sample.csv".endswith(".csv"))   # True
print("text.txt".endswith("txt", 0,8)) # True
print("text.txt".endswith("txt", 0,5)) # False


# 7. expandtabs(tabsize) – Expands tabs into spaces.
text = "1\t2\t3"
print(text.expandtabs())        # "1       2       3"
print(text.expandtabs(2))       # "1  2  3"
print("a\tb".expandtabs(4))     # "a   b"
print("\tPython".expandtabs(3)) # "   Python"
print("S\tR".expandtabs(1))     # "S R"


# 8. find(sub, start, end) – Returns index of first occurrence, -1 if not found.
text = "Shiva reddy"
print(text.find("a"))              # 4
print(text.find("reddy"))          # 6
print(text.find("Python"))         # -1 (not found)
print("banana".find("a"))          # 1
print("Assignment".find("s", 2))   # 2


# 9. format() – Formats string using placeholders.
print("Hello {}".format("Shiva"))                              # "Hello Shiva"
print("The number is {}".format(22))                           # "The number is 22"
print("Coordinates: {},{}".format(10, 20))                     # "Coordinates: 10, 20"
print("{0} + {0} = {1}".format(2,4))                           # "2 + 2 = 4"
print("Name: {name}, Age: {age}".format(name="Shiva", age=23)) # "Name: Shiva, Age: 23"
print("Sum is : {}".format(100+200+300))                       # Sum is : 600


# 10. index(sub, start, end) – Like find(), but raises error if not found.
text = "Shiva reddy"
print(text.index("a"))            # 4
print(text.index("reddy"))        # 6
# print(text.index("Python"))     # ValueError : String not found
print("banana".index("a"))        # 1
print("Assignment".index("s", 2)) # 2


# 11. isalnum() – True if all characters are alphanumeric.
print("@shiva1".isalnum())    # False
print("Python3".isalnum())    # True
print("2026".isalnum())       # True
print(" ".isalpha())          # False
print("Shiva".isalnum())      # True
print("a1b2c3".isalnum())     # True


# 12. isalpha() – True if all characters are alphabetic.
print("Shiva".isalpha())      # True
print("Shiva123".isalpha())   # False
print("Python".isalpha())     # True
print(" ".isalpha())          # False
print("ShIvA".isalpha())      # True


# 13. isascii() – True if all characters are ASCII.
print("Shiva".isascii())   # True
print("123".isascii())     # True
print("π".isascii())       # False
print("Python3".isascii()) # True
print("safé".isascii())    # False


# 14. isdecimal() – True if all characters are decimal numbers.
print("123".isdecimal())    # True
print("12.3".isdecimal())   # False
print("22/7".isdecimal())   # False
print("abc".isdecimal())    # False
print(" ".isdecimal())      # False


# 15. isdigit() – True if all characters are digits.
print("123".isdigit())       # True
print("²³".isdigit())        # True (superscript digits)
print("abc".isdigit())       # False
print("12.3".isdigit())      # False
print(".3".isdigit())        # False
print(" ".isdigit())         # False


# 16. isidentifier() – True if string is valid Python identifier.
print("variable".isidentifier())   # True
print("var123".isidentifier())     # True
print("123var".isidentifier())     # False
print("my_var".isidentifier())     # True
print("my-var".isidentifier())     # False


# 17. islower() – True if all letters are lowercase.
print("shiva".islower())      # True
print("Shiva".islower())      # False
print("123".islower())        # False
print("python@!_+".islower()) # True
print("!@#+".islower())       # False


# 18. isnumeric() – True if all characters are numeric.
print("123".isnumeric())      # True
print("12.3".isnumeric())     # False
print("SHIVA".isnumeric())    # False
print("abc123".isnumeric())   # False
print("²³".isnumeric())       # True (superscript)


# 19. isprintable() – True if string is printable.
print("Shiva!".isprintable())        # True
print("123".isprintable())           # True
print("\n".isprintable())            # False
print(" ".isprintable())             # True
print("Python\t3".isprintable())     # False


# 20. isspace() – True if all characters are whitespace.
print("   ".isspace())         # True
print("\t\n".isspace())        # True
print(" abc ".isspace())       # False
print(" a ".isspace())         # False
print("".isspace())            # False


# 21. istitle() – True if string is title cased (first letter of each word uppercase)
print("Shiva".istitle())           # True
print("Shiva reddy".istitle())     # False
print("Python Training".istitle()) # True
print("Python3".istitle())         # True
print("123 Python".istitle())      # True


# 22. isupper() – True if all letters are uppercase
print("SHIVA".isupper())     # True
print("Shiva".isupper())     # False
print("123".isupper())       # False
print("SHIVA!+".isupper())   # True
print("PYTHON3".isupper())   # True


# 23. join(iterable) – Joins elements of iterable into a string
print(",".join(["a", "b", "c"]))            # "a,b,c"
print(" ".join(["Python", "Training"]))     # "Python Training"
print("-".join(["12","05","2026"]))         # "12-05-2026"
print("".join(["P","y","t","h","o","n"]))   # "Python"
print("|".join(["apple","banana","mango"])) # "apple|banana|mango"


# 24. ljust(width, fillchar) – Left-justify string with optional fill
print("hi".ljust(5))        # "hi   "
print("hi".ljust(5, "-"))   # "hi---"
print("Python".ljust(10))   # "Python    "
print("123".ljust(6, "0"))  # "123000"
print("abc".ljust(5, "."))  # "abc.."


# 25. lower() – Converts string to lowercase
print("SHIVA".lower())       # "shiva"
print("Python3".lower())     # "python3"
print("ShIvA".lower())       # "shiva"
print("123ABC".lower())      # "123abc"
print("@12Ab".lower())       # "@12ab"


# 26. lstrip(chars) – Removes leading characters (default: whitespace)
print("   shiva".lstrip())     # "shiva"
print("###shiva".lstrip("#"))  # "shiva"
print("Shiva$$$".lstrip("$"))  # "Shiva$$$"
print("  Python  ".lstrip())   # "Python  "
print("0001230".lstrip("0"))   # "1230"


# 27. partition(sep) – Splits into 3 parts: before, sep, after  (gives tuple as output)
print("shiva reddy".partition(" "))      # ('shiva', ' ', 'reddy')
print("a-b-c".partition("-"))            # ('a', '-', 'b-c')
print("Python".partition("y"))           # ('P', 'y', 'thon')
print("Assessment".partition("ss"))      # ('A', 'ss', 'essment')
print("abc".partition("d"))              # ('abc', '', '')


# 28. replace(old, new, count) – Replaces substring
print("I like java".replace("java", "python"))  # "I like python"
print("banana".replace("a", "o"))               # "bonono"
print("hello world".replace("world", "Python")) # "hello Python"
print("aaaaa".replace("a", "b", 3))             # "bbbaa"
print("aaa bbb aaa".replace("bbb", "aaa"))      # "aaa aaa aaa"


# 29. rfind(sub, start, end) – Last occurrence of substring, -1 if not found
print("banana".rfind("a"))           # 5
print("Python pythOn".rfind("o"))    # 4
print("Python python".rfind("o"))    # 11
print("shiva reddy".rfind("Python")) # -1
print("Assessment".rfind("s"))       # 5
print("abcdabc".rfind("abc"))        # 4


# 30. rindex(sub, start, end) – Like rfind() but raises error if not found
print("banana".rindex("a"))             # 5
print("python Python".rindex("o"))      # 11
# print("hello world".rindex("Python")) # ValueError : substring not found
print("Assessment".rindex("s"))         # 5
print("abcdabc".rindex("abc"))          # 4


# 31. rjust(width, fillchar) – Right-justify string
print("hi".rjust(5))        # "   hi"
print("hi".rjust(5, "*"))   # "***hi"
print("Python".rjust(10))   # "    Python"
print("123".rjust(6, "0"))  # "000123"
print("abc".rjust(5, "."))  # "..abc"


# 32. rpartition(sep) – Splits into 3 parts from right: before, sep, after
print("Shiva reddy".rpartition(" "))  # ('Shiva', ' ', 'reddy')
print("a-b-c".rpartition("-"))        # ('a-b', '-', 'c')
print("Python".rpartition("y"))       # ('P', 'y', 'thon')
print("Assessment".rpartition("ss"))  # ('Asse', 'ss', 'ment')
print("abc".rpartition("x"))          # ('', '', 'abc')


# 33. rsplit(sep, maxsplit) – Splits from right into list
print("a-b-c".rsplit("-", 1))               # ['a-b', 'c']
print("a-b-c".rsplit("-"))                  # ['a', 'b', 'c']
print("one two three".rsplit(" ", 1))       # ['one two', 'three']
print("2026-05-12".rsplit("-", 2))          # ['2026', '05', '12']
print("apple,banana,cherry".rsplit(",", 1)) # ['apple,banana', 'cherry']
print("x-y-z".rsplit("-", 0))               # ['x-y-z']


# 34. rstrip(chars) – Removes trailing characters (default: whitespace)
print("   python   ".rstrip())   # "   python"
print("###a1###".rstrip("#"))    # "###a1"
print("$$$shiva$$$".rstrip("$")) # "$$$shiva"
print("  Python3  ".rstrip())    # "  Python3"
print("0123000".rstrip("0"))     # "0123"


# 35. split(sep, maxsplit) – Splits into list
print("python,fullstack,training".split(","))  # ['python', 'fullstack', 'training']
print("python is easy".split())                # ['python', 'is', 'easy']
print(".-p-y".split("-", 1))                   # ['.', 'p-y']
print("2026-05-12".split("-", 2))              # ['2026', '05', '12']
print("Python".split("y"))                     # ['P', 'thon']


# 36. splitlines(keepends) – Splits string at line breaks
text = "Python\nFullstack\nTraining"
print(text.splitlines())                  # ['Python', 'Fullstack', 'Training']
print(text.splitlines(True))              # ['Python\n', 'Fullstack\n', 'Training']
print("Python\r\nFullstack".splitlines()) # ['Python', 'Fullstack']
print("Python Training".splitlines())     # ['Python Training']
print("Python\nCode\n".splitlines())      # ['Python', 'Code']


# 37. startswith(prefix, start, end) – Checks start of string
text = "shiva reddy"
print(text.startswith("shiva"))           # True
print(text.startswith("reddy"))           # False
print("Python".startswith("Py"))          # True
print("python.py".startswith("python"))   # True
print("python.txt".startswith("txt", 7))  # True
print("python.txt".startswith("txt", 5))  # False


# 38. strip(chars) – Removes leading and trailing characters
print("   shiva   ".strip())        # "shiva"
print("###shiva###".strip("#"))     # "shiva"
print("$$$Python$$$".strip("$"))    # "Python"
print("  python  ".strip())         # "python"
print("000123000".strip("0"))       # "123"


# 39. swapcase() – Swap uppercase/lowercase
print("Shiva Reddy".swapcase())   # "sHIVA rEDDY"
print("Python3".swapcase())       # "pYTHON3"
print("ShIvA".swapcase())         # "sHiVa"
print("123ABC".swapcase())        # "123abc"
print("aBcDeF".swapcase())        # "AbCdEf"


# 40. title() – Capitalizes first letter of each word
print("shiva reddy".title())               # "Shiva Reddy"
print("python training".title())           # "Python Training"
print("java SCRIPT".title())               # "Java Script"
print("python training is easy".title())   # "Python Training Is Easy"
print("123abc def".title())                # "123Abc Def"


# 41. translate(table) – Replace characters using translation table
table = str.maketrans("abc", "123")
print("abcde".translate(table))                   # "123de"
table1 = str.maketrans({"x":"1","y":"2"})
print("xyz".translate(table1))                    # "12z"
table2 = str.maketrans("", "", "aeiou")
print("shiva".translate(table2))                  # "shv"
print("Python".translate(str.maketrans("P","p"))) # "python"
print("123".translate(str.maketrans("1","9")))    # "923"


# 42. upper() – Converts to uppercase
print("shiva".upper())      # "SHIVA"
print("Python3".upper())    # "PYTHON3"
print("ShIvA".upper())      # "SHIVA"
print("123abc".upper())     # "123ABC"
print(".py".upper())        # ".PY"


# 43. zfill(width) – Pads string on the left with zeros
print("7".zfill(3))       # "007"
print("42".zfill(5))      # "00042"
print("123".zfill(6))     # "000123"
print("Python".zfill(10)) # "0000Python"
print("".zfill(4))        # "0000"