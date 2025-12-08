# -----------------------------------Operators -----------------------------------------------
# Arithmatic Operators Example
# + , - , % , * , ** , /

a = 70
b = 20
# print("Addition of", a, "and", b, "is", a+b)
# print("Subtraction of", a, "and", b, "is", a-b)
# print("Multiplication of", a, "and", b, "is", a*b)
# print("Division of", a , "and", b, "is", a/b)
# print("Floor Division of", a , "and" , b , "is", a//b)  #Complete divisible number
# print("Modulus of", a , "and", b , "is", a%b)
# print("exponentiation of", a, "and", b , "is", a**b)


# Questions
#🔹 Arithmetic Operators (Tasks 11–20)

#11. Add two numbers and print the result.
#12 Multiply two numbers and print the result.
#13 Subtract two numbers and print the result.
#14 Divide two numbers and print the result.
#15. Use floor division (//) and print the result.
#16. Use modulo operator % to find remainder.
#17. Raise a number to a power using **.
#18 Combine multiple operations in one expression: 2 + 3 * 4 - 5. - Ask
#19 Calculate the average of 3 numbers.
#20 Use parentheses to change order of evaluation in an expression. - Ask 
# No1 = 145
# No2 = 56
# No3 = 86
# print(No1 + No2)
# print(No1*No2)
# print(No1 - No2)
# print(No1/No2)
# print(No1//No2)
# print(No1%No2)
# print(No1**No2)
# print(2 + 3*4 - 5)
# print((No1 + No2 + No3)/3)


#--------------------Assignment Operators
# = , +=, -=, *=, /=, %=, **=
# a = 5
# a**=2
# print("value of a is", a)


#--------------------------Comparison Operators 
# a = 5
# b = 5
# print("Is a equal to b?", a ==b) #True
# print("Is a not equal to b?", a !=b) #False
# print("Is a greater than b?", a>b) #False
# print("Is a less than b?", a < b) #False
# print("Is a greater than or equal to b?", a>=b) #True
# print("Is a less than or equal to b?", a <=b) #True


# Questions - 🔹 Comparison Operators (Tasks 21–30)
#21. Check if two numbers are equal.
#22. Check if one number is greater than another.
#23. Check if one number is less than or equal to another.
#24. Compare string variables for equality. - Need to ask
#25. Check if two different variables point to the same value. - Need to ask
#26. Use != to verify inequality.
#27. Combine comparison and arithmetic: a + 5 > b * 2.
#28. Compare float and integer values.
#29. Compare lengths of two strings using len().
#30. Compare two expressions using ==. 
# Number1 = 56
# Number2 = 58
# Float= 60.56
# Integer = 40
# print(Number1 == Number2) #21
# print(Number1 > Number2) #22
# print(Number1 <= Number2) #23
# Str1 = "Anjali"
# Str2 = "Tiwari"
# Str1 == Str2
# print(Str1[3] == Str2[3])
# print(Number1 != Number2)
# print(Number1 + 5 > Number2*2)
# print(Float >= Integer)
# print(len(Str1) >= len(Str2))
# print(Float == Integer)


#-----------------------Logical Operators-----------------------------------------------------------

# a = 5
# print("Using 'OR' operator", a%3==0 or a%5==0) #True
# print("using 'AND' operator", a%3==0 and a%5==0) #False

# 31. Use and to combine two True conditions.
# 32. Use or to check if at least one condition is True.
# 33. Use not to reverse a boolean value. - need to ask
# 34. Combine not with and or or.
# 35. Use logical operators to check if a number is between 1 and 10. - need to ask
# 36. Create a complex condition combining math and logic. - need to ask
# 37. Check if a string is not equal to "Python". - need to ask
# 38. Use boolean variables in a condition. - need to ask
# 39. Use nested comparisons: 10 > 5 > 2. - need to ask
# 40. Use if with a logical expression and print a message. - need to ask
# A = 25
# B = 20
# C = 17
# D = 20
# E = 8
# print("Via 'AND' Operator =", A%5 == 0 and C%5 == 0)
# print("Via 'OR' Operator =", A%5 == 0 or C%5 == 0)
# print(A!=B, B!=C, D!=B)
# print("Combine not with AND or OR:", A!=D and C!=B and B!=D , C!=D or A!=C)
# print(A >= B >= D >= E >= C)


#------------------------Increment / Decrement operator (a++, a--)

#Input 
# name = input("enter your name:")
# Age = int(input("enter age:"))
# Marks = float(input("Enter marks:"))
# Val = input("Enter some value:")
# print("you entered:", name)
# print(type(Val), Val)

#--------------------------------------🔹 Math Functions & Expressions (Tasks 41–50) - need to ask all
# 41. Find square root of a number using math.sqrt().
# 42. Use abs() to get absolute value. - abs stands for absolute value
# 43. Use pow() to calculate powers.
# 44. Round a float to 2 decimal places.
# 45. Use math.floor() and math.ceil() on float values.
# 46. Calculate area of a circle (use π from math.pi).
# 47. Use min() and max() with a list of numbers.
# 48. Use divmod() to get quotient and remainder.
# 49. Calculate factorial using math.factorial().
# 50. Use math.sin() or math.cos() on an angle (convert to radians).

# import math as m
# print(m.sqrt(64))
# print(m.sqrt(99))

# n: float = 52.369 #2nd ques -  abs = absolute value
# n1: int = 5
# n2: complex = 3 + 4j #need to know how it come 5.0
# print(abs(n))
# print(abs(n1))
# print(abs(n2))

# print(pow(5*3))



#--------Questions
#1. Write a  program to input 2 numbers & print their sum
# num1 = input("Enter the first number:")
# num2 = input("Enter the second number")
# sum = num1 + num2
# print(sum)


#2. Write a program to input side of a square & print its area
# Side = float(input("Enter the value of a side:"))
# Area = Side*Side
# print(Area)
#or
# Side = float(input("Enter the value of a side:"))
# print("Area:", Side*Side)


#3. Write a program to input 2 floating point number & print their average 
# number1 = float(input("Enter your first number:"))
# number2 = float(input("Enter your second number:"))
# Average = (number1+ number2)/2
# # print(Average)
# #or 
# print("Average:", (number1 + number2)/2)


#4 Write a program to input 2 int number, a and b
#print True if a is greater than or equal to b. if not print False
# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# print(a >= b)


#----------Questions based on operators--------------------------
 
#1 You are given two variables, height1 and height2 - use relational operators to output False, False if they are equal, else True
# height1 = 15
# height2 = 13
# print(height1 == height2)


#2 Write a program to reverse an integer in python
# A = "Anjali-Tiwari"
# print(len(A))
# for I in range (len(A)-1, -1, -1):
#     print(A[I], I)


#3 What is the output of the following addition (+) operator (Ask - 10, 20 and 10, 20, 30, 40)
# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)


#4 What is the output of the expression  print(-18 // 4) (Ask= Ans 4 accorsing to my understanding)
# a  = 18
# b = 4
# print(-18//4)


#5 What is the value of the following Python Expression - 9.0
# print(36/4)


#6 4 is 100 in binary and 11 is 1011. What is the output of the following bitwise operators? - Ask
# a = 4
# b = 11
# print(a | b)
# print(a >> 2)


#7 What is the output of the following assignment operator - Ans = 10 
# y = 10
# x = y 
# y+= 2
# print(x)


#8 What is the output of print(2 * 3 ** 3 * 4) - Ans = 216
# print(2 * 3 ** 3 * 4) 


#9 What is the output of the following Python code - Ans = 100, True (ask)
# x = 10
# y = 50
# if x ** 2 > 100 and y < 100:
#     print(x, y)


# 10 What is the output of the following code - Ans = 36 , 3
# x = 6
# y = 2
# print(x ** y)
# print(x // y)


#11 What is the output of the following code - Ask 
# x = 100
# y = 50
# print(x and y)


#12 What is the output of print(2%6) - Ans = value error - Ask 
# print(2%6)


#13 Remember, we have not used brackets here. And Exponent operator ** has right-to-left associativity in Python.
# print(2 ** 3 ** 2)


#14. What is the output of the following code - Ask 
# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))


#15 What is the output of the following code? - Ask 
# print(10 - 4 * 2)
# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")
# print(sampleList)


#16 What is the output of the following code? - dno but answer is maj
# var= "James Bond"
# print(var[2::-1])

#17  What is the output of the following code? - Ask 
# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)    


#18 What is the output of the following code? - Ask 
# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)
# calculate(5, 6)


#19 . What is the output of the following code?
# for i in range(10, 15, 1):
#   print( i, end=', ')

#20 . What is the Output of the following code? - ask 
# for x in range(0.5, 5.5, 0.5):
#   print(x)


#21 What is the output of the following- Ask 
# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)


#22 What is the output of the following code? - Ask 
# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]
# print(listOne == listTwo) - True
# print(listOne is listTwo) - True


# # 10. What is the output of the following code?b- need to ask 
# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)
# calculate(5, 6)
# Hint: functions in Python
# 20
# The program executed with errors
# 30
# Explanation
# In Python, we can set default values for arguments. If the function is called without the argument, the default value is used.


#1. What is the output of the following code - Ask 
# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))


# 7. Please select the correct expression to reassign a global variable “x” to 20 inside a function fun1() - need to ask 
# x = 50
# def fun1():
#     # your code to assign global x = 20
# fun1()
# print(x) # it should print 20


# 8. What is the output of the following variable assignment?
# x = 75
# def myfunc():
#     x = x + 1
#     print(x)
# myfunc()
# print(x)




