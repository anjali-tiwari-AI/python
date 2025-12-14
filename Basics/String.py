# Duplicate or copy past (Alt + Shift + downarrow)


#----------Indexing in string------------------------
# Single = input("Enter the string: ")
# print(Single[2])

# Index = input("Enter the string: ")
# print(Index[1 : :])


#-----------Slicing--------------------------------
#Syntax = String[Start : End : Step ]
# Slicing = input("Enter the string: ")
# print(Slicing[1 :]) #start from one till the end point
# print(Slicing[ :4]) #start from 1 upto 4
# print(Slicing[ : ]) # Will give start to end point
# print(Slicing[ : :-2]) #Step indexing
# print(Slicing[0:5])
# print(Slicing[1 : len(Slicing) : 1])


#--------------Basic operations in string (Concatenation , Repetation , Membership, len , escape character )----------------------
# First_name = input("Enter the user first name: ")
# Last_name = input("Enter the user last name: ")
# print(First_name + " " + Last_name) # Concatenation
# print(First_name * 3) # Repetation
# print("j" in First_name) # Membership
# print("z" not in First_name) # Not a Membership
# print(len(First_name + Last_name)) # Gives length of the string





# print(dir(str))
# print(dir(str))

"""['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
 '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', 
 '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', 
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']"""


#=========================== DONE ===============================================================================================================
#1 Write a method in which you will "remove" any given character from a string
# String = input('Enter the string:')
# Removing = input("Enter the character which you wants to remove from string: ")
# print(String.replace(Removing , " "))


#=============== DONE =============================================================================================================================================
#2 Write a program to count occurrences of a given character in a string
# Occurrences = input("Enter the string: ")
# Given_character = input("Enter the character from a string to count occurrences of it: ")
# count = 0

# for i in Occurrences:
#     if i == Given_character:
#         count += 1
#     else:
#         continue
# print(f"The total {i} is: {count}")  
        
    

#===============================================================================================================================================================================
#3 Write a program to check if two strings are Anagram  - (Check : Heart and earth) - Sort method (by default it is in ascending order)
# Anagram1 = input('Enter the first string:- ')
# Anagram2 = input("Enter the second string:- ")

# if len(Anagram1) != len(Anagram2):
#     print("No, it is not Anagram i.e. both are", Anagram1, "and", Anagram2)
# else:
#     if sorted(Anagram1) == sorted(Anagram2):
#         print("Yes, it is anagram i.e. both are", Anagram1 , "and",  Anagram2)
#     else:
#         print("No, it is not anagram i.e. both are", Anagram1 , "and",  Anagram2)
               


#======================== DONE ===================================================================================================================
#4 Write a program to check a string is palindrome or not
# Palindrome = input("Enter the value to check if it is palindrome or not: ")
# Pal = []
# for i in Palindrome:
#     Pal.append(i)

# i = 0
# j = -1

# for k in range(len(Palindrome)):
#     if Palindrome[i] == Pal[j]:
#         print("Yes, it is palindrome i.e.:", Palindrome)
#         i += 1
#         j -= 1
#     else:
#         print("No, it is not palindrome i.e.:", Pal)
#         break
    

#=============================== DONE ====================================================================================================================
#5 Write a program to check given character is vowel or consonant
# Vowel = "AEIOUaeiou"

# Vowel_or_Consonant = input("Enter the character to check it is vowel or consonant: ")

# for i in Vowel_or_Consonant:
#     if i in Vowel:
#         print("Yes, the entered character is vowel i.e ", Vowel_or_Consonant)
#     else:
#         print("No, the entered character is not vowel i.e. ", Vowel_or_Consonant)



# char = input('Enter the character: ').lower()

# if len(char) == 1 and char.isalpha():
#     if char in "aeiou":
#         print('Yes, the entered character is vowel i.e.', char)
#     else:
#         print("No, the entered character is not vowel i.e.", char)
# else:
#     print("Please enter the single alphabet character")
    
    
#================= DONE ============================================================================================================================
#6 Write a program to check given character is digit or not
# Digit_or_not = input("Enter the value: ")

# if len(Digit_or_not) >=0 and Digit_or_not.isdigit():
#     print("Yes, the entered character is digit i.e.:", Digit_or_not)
# else:
#     print("No, the entered character is not digit becuase you have extered:", Digit_or_not )


#================================================================================================================================================
#7 Write a program to replace the string space with a given character
# Character = input('Enter the character which you wants to place in a string space:')
# String = input('Enter the sentence: ')

# for i in String:
#     if i == " ":
#         i.replace(" ", Character)

#     else:
#         pass



#========================================================================================================================================
#8 Write a program to convert lowercase character to uppercase of string
#9 Write a program to convert lowercase vowels to uppercase in string
#10 Write a program to delete vowels in a given string
#11 Write a program to count Occurrence of Vowels  and consonant in a  string
#12 Write a program to print the highest frequency character in a string
#13 Write a program to replace first occurrence of Vowel with " - " in string
#14 Write a program to count alphabets, digits and special characters
#15 Write a program to separate characters in a given string
#16 Write a program to remove blank space from string
#17 Write a program to concatenate two strings
#18 Write a program to remove repeated character from string
#19 Write a program to calculate sum of integers in string
#20 Write a program to print all non repeating character in string
#21 Write a program to copy one string to another string
#22 Write a program to sort characters of string
#23 Write a program to sort character of string in descending order
