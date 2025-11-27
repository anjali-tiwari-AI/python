# def function_name(parameters or params):
#     function body
#     return result

# function_name = Name of the function
# parameters = inputs required in a function
# Body = logic code of a function
# Return = result/output

# def add(a,b):
#     print(a+b)

# def addition(a,b):
#     return a+b
# def function_name(parameters/params):
#     Function logic
#     return result




# def evenOdd(a):
#     if (a%2==0):
#         print("Number is even")
#     else:
#         print("Number is odd")

# evenOdd(4)
# evenOdd(5)
# evenOdd(67)
# evenOdd(89)
# evenOdd(45)
# evenOdd(35)


# def multiplication(s,r,t):
#     return s*r*t

# SI=multiplication(100,5,10)/100
# CI=multiplication(100,5,10)*100
# DI=multiplication(100,5,10)+100
# EI=multiplication(100,5,10)-100


# print("Simple interest is ", SI)



# def likho():
#     print ("Hello World")
# likho()

# def addition(a,b):
#     return a+b
# x=addition(4,5)
# print(x)


# def greeting(name,age):
#     print(f"Hello {name} , your age is {age}")


# greeting("Anjali",24)
# greeting("Rajat",25)
# greeting("Chetan",26)

# print("without keyword")
# greeting(27,"Anjali")

# print("with keyword")
# greeting(age=27,name="Anjali")


#---already entered name-----
# def hello(name="Guest"):
#     print("Hello",name)

# hello()


#---MULTIPLE THINGS-----
# def addition(*args):
#     print(sum(args))

# addition(12,13,14,15)


#--multiple things with keys
# def stu_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# stu_info(Name="Anjali",Age=23,City="Indore",Section="CSE",fees=20000)

# x=50 #Global
# def scope():
#     x=24 #Local /Temp variable
#     print("Inside Function , value of x is : ",x)

# scope()
# print("outside Function , value of x is : ",x)



# def even_odd(a):
#     if(a%2==0):
#         return f"Number is even"
#     else:
#         print("Number is odd")

# # even_odd(23)
# even_odd(22)


# def list_ops(c):
#     print("Length of list",len(c))
#     print("Min value of list",min(c))
#     print("Max value of list",max(c))
#     print("Sum of all elements",sum(c))
#     c.sort()
#     print("Ascending",c)
#     c.sort(reverse=True)
#     print("Descending",c)   

# a=[1,2,3,4,5,2,7,664,9,1]

# list_ops(a)


#============PRACTICE QUESTIONS====================================================================================
#  Basic Level (50 Questions) 
# Focus: function definition, calling, parameters, return values, scope basics. 


#========================DONE=======================================================================================
# 1. Write a function that prints "Hello, World!". 
# def funct():
#     print("Hello, World!")
# funct()

#======================DONE======================================================================================
# 2. Create a function that takes a number and prints whether it is even or odd. 
# def even_odd(Num):
#     Number = int(input("Enter the nummber:"))
#     if Number%2 == 0:
#         print("The entered number is even i.e.", Number)
#     else: 
#         print("The entered number is odd i.e.", Number)
# even_odd(50)


#==================DONE============================================================================================
# 3. Write a function that adds two numbers and returns the result. 
# def add_2_number(a, b):
#     Add = a + b
#     return Add
# print(add_2_number(15, 16))    


#=====================DONE========================================================================================
# 4. Define a function that returns the square of a number. 
# def Square_of_number(A):
#     Square = A*A
#     print(Square)
# Square_of_number(5)
    

#================DONE===========================================================================================
# 5. Create a function to find the maximum of two numbers. 
# def maximum(a ,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# maximum(152, 15)


#===============DONE=================================================================================================
# 6. Write a function that converts Celsius to Fahrenheit. 
# def Celsius_to_Fahrenheit():
#     Celsius = int(input("Enter the Celsius to converts Fahrenheit:"))
#     Fahrenheit = (Celsius*9/5) + 32
#     print(Fahrenheit)
# Celsius_to_Fahrenheit()

#===============DONE===================================================================================================
# 7. Make a function that returns the factorial of a number (using loop). 
# def Factorial():
#     Fact = int(input("Enter the number: "))
#     Num = 1
#     for i in range(1, Fact+1):
#         Num = Num*i
#     print("The Factorial of a number:", Fact , "is", Num)
# Factorial()


#==================DONE===========================================================================================
# 8. Write a function to calculate the area of a rectangle. 
# def Area_of_Rectangle():
#     Length =  int(input("Enter the Length of the rectangle: "))
#     Width = int(input("Enter the width of the rectangle: "))
#     Area = Length * Width
#     return "the area of a rectangle is" , Area
# print(Area_of_Rectangle())


#====================DONE=========================================================================================
# 9. Create a function that accepts a name and prints a greeting message. 
# def Greeting(Name = "Sir/Madam"):
#     Name = input("Enter your name:")
#     print(f"Hello {Name}, welcome to this Taj hotel")
# Greeting()

# #-----------------------------------------------------
# def Greeting(Name = "Sir/Madam"):
#     print(f"Hello {Name}, welcome to this Taj hotel")
# Greeting()


#====================DONE=========================================================================================
# 10. Write a function to check if a number is positive, negative, or zero.
# def Positive_Negative_Zero():
#     Number = int(input("Enter the number: "))
#     if Number>=1:
#         print("Entered number is positive i.e.", Number)
#     elif Number<-1:
#         print("Entered number is negative i.e.", Number)
#     else:
#         print("Entered number is Zero")
# Positive_Negative_Zero()


#===============DONE============================================================================================== 
# 11. Write a function that returns the length of a string. 
# def length_string():
#     String = input("Enter the string here: ")
#     print(len(String))


#-----------------------------
# def length_string():
#     count = 0
#     String = input("Enter the string: ")
#     for char in String:
#         count += 1
#     print("The length of the string is:", count)
 


#=============NEED TO CHECK========================================================================================
# 12. Create a function that reverses a string. 
# def Reverse_string():
#     Reverse = input('Enter the string to reverse it: ')
#     Reversed = []
#     for char in Reverse(-1, 0, -1):
#         print(char)
# Reverse_string()



#====================NEED TO CHECK==============================================================================
# 13. Define a function to check if a number is prime. 
# def prime():                
#     count = 0
#     Number = int(input("Enter the numbers: "))
#     for i in Number():
#         if Number%i == 0:
#             count += 1
#         else:
#             pass 
#         for j in Number:
#             if count>2:
#                 pass
#             else:
#                 print("The entered number is prime: ", Number)       
# prime()


#======================NEED TO CHECK============================================================================
# 14. Write a function to calculate the sum of first n natural numbers.
# def sum_of_number(*args):
#     Sum = 0
#     for i in args:
#         Sum = Sum + i
#         return Sum
# print(sum_of_number(1, 2, 3, 4, 5, 6, 7, 8, 9))


#==================NEED TO CHECK============================================================================== 
# 15. Write a function that multiplies all numbers in a list. 
# def multiplies_all_numbers():
#     List = int(input("Enter the numbers: "))
#     List_number = int(input(range(List("Enter the list numbers: "))))
#     Multi = 1
#     for i in List_number():
#         Multi = Multi*i
# multiplies_all_numbers()       


#==================DONE===============================================================================================
# 16. Make a function that prints the first 10 Fibonacci numbers. 
# def Fibonacci_numbers(i):
#     Fibonacci_10_No = int(input("Enter the number:"))
#     i = 0
#     First = 0
#     Second = 1
#     while i <= Fibonacci_10_No:
#         Third = First + Second
#         First = Second
#         Second = Third
#         i += 1
#         print(f"The {i} fibonacci number is : {Third}")


#====================NEED TO CHECK============================================================================================
# 17. Write a function to check if a string is a palindrome. 
# def string_is_palindrome(*args):
#     Palindrome = str(input("Enter the string: "))
#     Pal = []
#     for (i) in Palindrome():
#         Pal.append(i)
#         print(i, end = "")
#     for j in Pal:
#         k = 0
#         if Pal[j] == Palindrome[-k]:
#             print("entered string is palindrome:" , Pal)
#         else:
#             print("Entered string is not palindrome:", Pal)
#         k -= 1
# string_is_palindrome()             


#===============NEED TO CHECK=======================================================================================================
# 18. Create a function to find the minimum number in a list. 
# def Minimum_no(*args):
#     List = int(input("Enter the numbers:"))
#     Listing = []
#     for j in List:
        
#         print(List)
# Minimum_no()

#===================DONE==================================================================================================
# 19. Write a function that returns the average of numbers in a list. 
# def average_of_number():
#     A = []
#     Sum = 0
#     List = int(input("Enter the number of times of the numbers: ")) 
#     for i in range(List):
#        Number = int(input("Enter the number for whon you need average: "))
#        A.append(Number)
#     for j in A:
#         Sum = Sum + j
#         Average = Sum/List
#     else:
#         print(f"The average of the entered numbers is {Average}")
       

#===================DONE================================================================================================
# 20. Define a function that prints a multiplication table of a given number. 
# def multiplication_table():
    
#     Table = int(input("Multiplication Table of the number:"))
#     Num = Table
#     for i in range(1, 11):
#         Number = Num * i
#         print(f"{Num} x {i} = {Number}")
        


#==================== DONE ==============================================================================================
# 21. Write a function that returns the largest of three numbers. 
# def largest_of_3_numbers():
#     Largest = int(input("Number of times you wants to enter number: "))
#     Lrg = []
#     j = 0
#     for i in range(Largest):
#         Large = int(input("Enter numbers: "))
#         Lrg.append(Large)
        
#     if Lrg[j] > Lrg[j + 1] and Lrg[j] > Lrg[j + 2]:
#         print("The largest number is: ", Lrg[j])
        
#     elif Lrg[j] < Lrg[j + 1] and Lrg[j + 1] > Lrg[j + 2]:
#         print("The largest number is :", Lrg[j + 1])
        
#     else:
#         print("The largest number is :", Lrg[j + 2])
                 


#====================DONE=================================================================================================
# 22. Create a function to count the number of vowels in a string. 
# def Number_of_vowels():
#     Vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
#     String = input("Enter the string: ")
#     count = 0
#     for i in String:
#         if i in Vowels:
#             count += 1
#     else:
#         print(f"The number of vowels is {count}")

# Number_of_vowels()


#====================== NEED TO CHECK ============================================================================================
# 23. Write a function that checks if a number is Armstrong or not. 
# def Number_is_armstrong_or_not():
#     Number = int(input("Enter the number: "))
#     Num = Number
#     Sum = 0
#     count = int(input("Enter the number is digits in the entered number: "))

#     for i in Num():
#         Sum_Add = i**count
#         Sum = Sum_Add + Sum
#         print(Sum)
        
#     if Sum == Number:
#         print("Entered number is Armstrong: ", Number)
#     else:
#         print("Entered number is not Armstrong: ", Number)


# Number_is_armstrong_or_not()    
        

#===================== DONE ===============================================================================================
# 24. Define a function that takes a list and returns a new list with unique elements. 
# def Takes_list():
#     All_digits_list = list(input("Entered the numbers: "))
#     Unique_List = []
#     for i in All_digits_list:
#         if i not in Unique_List:
#             Unique_List.append(i)
#     else:
#         print(Unique_List)
        
  

#==================== DONE ==============================================================================================
# 25. Write a function to calculate simple interest. 
# def Simple_interest():
#     Principle = int(input("Enter the principle amount: "))
#     Time = float(input("Enter the duration of the time: "))
#     Rate = float(input("Enter the rate of interest: "))
#     SI = (Principle*Rate*Time)/100
#     print(SI)



#=================================================================================================================
# 26. Create a function that converts kilometers to miles. 
# def converts_kilometers_to_miles():
#     Kilometers = int(input('Enter the kilometer: '))
#     Miles = 0.621371
#     Kilo_to_mile = Kilometers*Miles
#     print(Kilo_to_mile)


#============== DONE =======================================================================================================
# 27. Write a function that swaps two numbers. 
# def swaps_two_numbers():
#     First = int(input('Enter the number: '))
#     Second = int(input("Enter the number: "))
#     print("Before swaping the numbers is: ", First , "and" , Second)
#     First , Second = Second , First
#     print("After swaping the numbers is: ", First , "and", Second)


#=============== DONE ==================================================================================================
# 28. Make a function that returns the sum of digits of a number. 
# def sum_of_digits_of_number():
#     Total = 0
#     Number = int(input("Enter the number: "))
#     while Number > 0:
#         Sum = Number%10
#         Total = Total + Sum
#         Number = Number//10
#     else:
#         print(Total)
# sum_of_digits_of_number()


#================ DONE ===================================================================================================
# 29. Write a function to count the number of words in a string. 
# def count_number_of_words_in_string():
#     Words = input("Enter the sentence here: ")
#     Number_of_words= 0
#     for i in Words:
#         if i == " ":
#             continue
#         Number_of_words += 1
#         print (f'The word is "{i}" and the Number is {Number_of_words}')
        


#================= NEED TO CHECK ====================================================================================================
# 30. Define a function that returns the ASCII value of a character. 


#============== NEED TO CHECK ==================================================================================================
# 31. Write a function that returns the maximum element in a tuple. 
# def Maximum_element_in_Tuple():
#     Tuple_counting = int(input("Write the total numbers (Counting) you wants to enter: "))
#     for i in Tuple_counting:
#         Tuple = tuple(input("Enter the elements: "))
#         print(max(Tuple))

# Maximum_element_in_Tuple()


#================ DONE ========================================================================================================
# 32. Create a function that checks if a character is a vowel. 
# def character_is_vowel():
#     Vowels = "AEIOUaeiou"
#     Character = input("Enter the character: ")
#     for i in Character:
#         if i in Vowels:
#             print(f"{True}, The entered character is vowels i.e. {Character}")
#         else:
#             print(f"{False}, The entered character is consonent (Not Vowel) i.e. {Character}")
# character_is_vowel()
    

#================ DONE =====================================================================================================
# 33. Write a function that calculates compound interest. 
# def compound_interest():
#     Principle = float(input("Enter the principle amount: "))
#     Rate = float(input("Enter the rate of interest: "))
#     Time = float(input("Enter the time: "))
#     CI = Principle*(1 + (Rate/100))**Time
#     print(CI)
# compound_interest()
  

#================ DONE =================================================================================================
# 34. Make a function to return the square root of a number. 
# (√N ≈ Initial Guess + (N - Initial Guess²)/ (2 x Initial Guess) 
# def Square_root_of_number():
#     Initial_Guess = int(input("Enter the number: "))
#     Result = Initial_Guess ** (0.5)
#     print("The square root of a number is", Result)


#============= DONE BUT NEED TO ASK ========================================================================================================
# 35. Write a function that takes two lists and returns their concatenation. 
# def takes_two_lists_and_returns_their_concatenation():
#     List_1 = list(input("The first list is: "))
#     List_2 = list(input("The second list is: "))
#     Final_list = (List_1 + List_2)
#     if Final_list == "":
#         pass 
#     print(Final_list)
# takes_two_lists_and_returns_their_concatenation()


#=============== DONE BUT NEED TO ASK ================================================================================================
# 36. Define a function that removes duplicates from a list. 
# def Removes_duplicates_from_list():
#     Original_list = list(input("Enter the details here: "))
#     Without_Duplicacy = []
#     for i in Original_list:
#         if i not in Without_Duplicacy:
#             Without_Duplicacy.append(i)
#             print(Without_Duplicacy)


#================ DONE ====================================================================================================
# 37. Create a function to check if a year is a leap year. 
# def leap_year():
#     Year = int(input("Enter the year: "))
#     if Year%4 == 0:
#         print("Yes, This is a leap year i.e.", Year)
#     else:
#         print("No, This is not a leap year i.e.", Year)
# leap_year()


#================= NEED TO CHECK ================================================================================================
# 38. Write a function that checks if a string contains only digits. 
# def checks_if_string_contains_only_digits():
#     Digits = input("Enter the string here: ")
#     Number = "1234567890"
#     i = 1
#     for i in range(Digits): 
#         if Digits // i == 0 or Digits % i == 0:
#             i += 1
#             print("Yes, it is ")
#         else:
#             print("No, it is not")
# checks_if_string_contains_only_digits()


#================= DONE ===================================================================================================
# 39. Write a function that converts hours into minutes. 
# def convert_hours_to_minutes():
#     Hours = int(input("Enter the number of hours: "))
#     Hours_to_minutes = Hours * 60
#     print(f"After converting {Hours} hour into minutes, it will be {Hours_to_minutes} minutes")


#============== DONE ===================================================================================================
# 40. Make a function to return the cube of a number. 
# def cube_of_number():
#     Number = int(input("Enter the number: "))
#     Cube = Number**3
#     print(f"the cube of a number {Number} is {Cube}")
# cube_of_number()


#====================== DONE ==============================================================================================
# 41. Write a function that checks if a number is divisible by another. 
# def number_is_divisible_by_another():
#     Num = int(input("Enter the number: "))
#     Divisible = int(input(f"Enter the number which you wants to divide from {Num} number: "))
#     if Num % Divisible == 0:
#         print(f"Yes, the entered number {Num} is divisible from {Divisible}")
#     else:
#         print(f"No, the entered number {Num} is not divisible from {Divisible}")
# number_is_divisible_by_another()     
    

#================ NEED TO CHECK =================================================================================================
# 42. Define a function that returns the absolute value of a number. 
# def absolute_value_of_number():
    
    

#=====================================================================================================================
# 43. Write a function to calculate perimeter of a circle. 
# def perimeter_of_circle():
#     Radius = int(input("Enter the radius of the circle: "))
#     Perimeter = 2*(22/7)*Radius
#     print(Perimeter)


#============= NEED TO CHECK =======================================================================================================
# 44. Create a function that prints a list in reverse order. 
# def list_reverse_order():
#     # Count = int(input("Enter the number of the list: "))
#     # New_List = []
#     # for i in Count:
#         List = list(input("Enter the list here: "))
#         New_List = List[ : :-1]
#         print(New_List)
# list_reverse_order()


#=============== DONE ====================================================================================================
# 45. Write a function that calculates the power of a number. 
# def power_of_number():
#     Number = int(input("Enter the number: "))
#     Power = int(input("Enter the power of the number: "))
#     Power_of_number = Number ** Power
#     print(f"The power of the {Number} is {Power_of_number}")
    
# power_of_number() 
    

#==================== DONE ==============================================================================================
# 46. Make a function that counts uppercase letters in a string. 
# def counts_uppercase_letters_in_string():
#     String = input("Enter the string: ")
#     count = 0
#     for char in String:
#         if char.isupper():
#             count += 1
#     else:
#         print("The total upper case in the String is", count)
        
# counts_uppercase_letters_in_string()       


#================ DONE ==================================================================================================
# # 47. Write a function that counts lowercase letters in a string. 
# def counts_lowercase_letters_in_string():
#     String = input("Enter the string here: ")
#     count = 0
#     for char in String:
#         if char.islower():
#             count += 1
#     else:
#         print("The total number of lowercase is", count)
# counts_lowercase_letters_in_string()


#============ NEED TO CHECK =====================================================================================================
# 48. Define a function that finds the HCF of two numbers. 
# def HCF_of_two_numbers():
#     First_no = int(input('Enter the number: '))
#     Second_no = int(input("Enter the second number: "))
#     First_HCF = []
#     Second_HCF = []
#     i = 1
#     for i in First_no():
#         First_no//i 
#         First_HCF.append(i)
#         print(First_HCF)
            
# HCF_of_two_numbers()

#===================== NNED TO ASK ============================================================================================
# 49. Create a function that finds the LCM of two numbers. 
# def LCM_of_two_numbers():
# #   "Calculates the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm"
#     First_no = int(input("Enter the first number: "))
#     Second_no = int(input("Enter the second number: "))
#     GCD = 0
#     for i in range (First_no and Second_no):
#         j = i+1
#         if First_no//(j) == 0 and Second_no//(j) == 0:
#             GCD.append(j)
#             j = i
#             print(GCD)
#         else:
#             continue
# LCM_of_two_numbers()

#============== NEED TO CHECK ======================================================================================================
# 50. Write a function that checks if a number is perfect. 

# def number_is_perfect():
#     Perfect = int(input("Enter the number: "))
#     Per_no = []
#     i = 1
#     while i == Perfect:
#         if Perfect % i == 0:
#             Per_no.append(i)
#             i += 1
#             print(Per_no)
#         else:
#             continue

# def Add_of_divisers():
#     Add = 0
#     for j in Per_no:
#         Add += j
#         print(Add)

# number_is_perfect() 
# Add_of_divisers() 



#============================================================================================================================================

# • Intermediate Level (50 Questions) 
# Focus: default arguments, keyword arguments, recursion, variable scope, higher-order functions, 
# lambda, *args and **kwargs. 

#======================= DONE ========================================================================================================================
# 1. Write a function with default parameters for a greeting message. 
# def default_parameters_for_greeting_message(Name = "Dear"):
#     print(f"Hello {Name}, welcome to this platform")
    
# default_parameters_for_greeting_message("Anjali")

#--------------------------
# def hello(name="Guest"):
#     print("Hello",name)

print("hello")


#================================================================================================================================================
# 2. Create a recursive function to calculate factorial of a number. 


#================================================================================================================
# 3. Write a recursive function to print Fibonacci sequence. 
# 4. Define a function that accepts *args and returns their sum. 
# 5. Create a function that accepts **kwargs and prints them. 
# 6. Write a function that uses both *args and **kwargs. 
# 7. Make a function that checks if a string is an anagram of another. 
# 8. Write a recursive function to find the sum of digits of a number. 
# 9. Define a function that returns the nth Fibonacci number. 
# 10. Create a function to flatten a nested list. 
# 11. Write a function that uses a lambda to square numbers. 
# 12. Write a function that uses map() to double elements of a list. 
# 13. Create a function that uses filter() to get even numbers from a list. 
# 14. Write a function that uses reduce() to compute product of numbers in a list. 
# 15. Make a function to calculate gcd using recursion. 
# 16. Create a function that implements binary search. 
# 17. Write a recursive function to reverse a string. 
# 18. Define a function that demonstrates local vs global variables. 
# 19. Write a function that returns the intersection of two lists. 
# 20. Create a function that returns the union of two sets. 
# 21. Write a function that counts frequency of elements in a list. 
# 22. Make a function that finds the longest word in a string. 
# 23. Write a function that accepts another function as argument. 
# 24. Create a decorator that logs the execution time of a function. 
# 25. Write a function to check if a string is pangram. 
# 26. Define a recursive function to find power of a number. 
# 27. Write a function that returns prime numbers in a range. 
# 28. Create a function that finds the second largest element in a list. 
# 29. Write a function that counts consonants in a string. 
# 30. Define a function that accepts a list of strings and returns the longest. 
# 31. Write a function that checks if a number is a strong number. 
# 32. Create a function that prints Pascal’s triangle up to n rows. 
# 33. Write a function that uses recursion to calculate gcd. 
# 34. Make a function that generates all prime numbers up to n. 
# 35. Write a function that accepts a function and a list and applies the function. 
# 36. Define a function that sorts a list without using built-in sort. 
# 37. Write a function to check if two strings are rotations of each other. 
# 38. Create a function that returns all factors of a number. 
# 39. Write a function to implement linear search. 
# 40. Define a function that accepts a string and counts digits, letters, spaces. 
# 41. Write a recursive function to calculate sum of first n natural numbers. 
# 42. Create a function that implements selection sort. 
# 43. Write a function that checks if a number is palindrome. 
# 44. Define a recursive function to generate all subsets of a list. 
# 45. Write a function that calculates digital root of a number. 
# 46. Create a function that prints all permutations of a string. 
# 47. Write a function that accepts two functions and returns their composition. 
# 48. Define a function that memoizes Fibonacci using dictionary. 
# 49. Write a function that demonstrates closure in Python. 
# 50. Create a function that returns a lambda function for power calculation. 

