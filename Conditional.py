#1 WAP to check whether an integer entered by thr user is odd or even - Done 
# Integer = int(input("Enter the number:"))
# if Integer%2 == 0:
#     print("it is a even number")
# else: 
#     print("it is an odd number")


#2 WAP to find the largest number among three number using conditional operator. - if last digit end with 9 than it can
# largest and first digit startes with 1 then i can be shortlest - Done
# A = int(input("Enter first number:"))
# B = int(input("Enter second number:"))
# C = int(input("Enter third number:"))
# if A>B and A>C:
#     print("A is the gratest number")
# elif B>C and B>A:
#     print("B is the greatest number")
# else:
#     print("C is the greatest number")


#3 WAP to find the largest number among three number. - second method to solve
# A = 11
# B = 15
# C = 90
# if A>B:
#     if A>C:
#         print("A is the greatest number")
# elif B>A:
#     if B>C:
#         print("B is the greatest number")
# else:
#     print("C is the greatest number")
# ------OR --------------
# print(max(A, B, C))


#4 WAP to find the largest among three variables using nesting if. - Need to check
# Number1 = int(input("Enter 1st number:"))
# Number2 = int(input("Enter 2nd number:"))
# Number3 = int(input("Enter 3rd number:"))
# if Number1> Number2:
#     if Number1>Number3:
#         print("Number 1 is the greatest number")
# elif Number2>Number1:
#     if Number2>= Number3:
#         print("Number 2 is the greatest number")
# else:
#     print("Number 3 is the greatest number")



#5 WAP to check the leap year using conditioal operator.- Done 
# Year = int(input("Enter year:"))
# if Year%4 == 0:
#     print("it is a leap year")
# else: 
#     print("it is not a leap year")


#6 WAP to check alphabets using conditional operator - Done
# Char = input("Enter alphabet:")
# if (Char>="A" and Char<="Z"):
#     print("It is a alphabate")
# elif (Char>="a" and Char<="z"):
#     print("it is a alphabate")
# else:
#     print("it is not a alphabate")


#7 WAP to check number is positive, negative, zero. - Done
# Num = int(input("Enter the number:"))
# if Num >= 1 and Num<=+Num:
#     print("It is positive number")
# elif Num<= -1:
#     print("it is a negative number")
# else:
#     print("it is a zero")


#8 WAP to check uppercase or lowercase alphabets. - Done
# Case = input("Enter the word:")
# if Case >= "A" and Case<= "Z":
#     print("it is uppercase")
# else:
#     print("it is lowercase")


#9 WAP to check entered character vowel or consonant. - Need to check
# char = input("Enter the character:")
# if char == ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
#     print(" it is Vowel")
# else:
#     print("it is a consonant")

# str = (AEIOUaeiou)
# char = input("enter:")
# if char == :
#     print(" it is Vowel")
# else:
#     print("it is a consonant")


#10 WAP to check whether a character is alphabet, digit or special character. - need to check
# char = int(input("Enter the data:"))
# if char<= 0 and char>= -1:
#     print("it is a digit")
# elif str(char<= "A" and char<="Z") or str(char>="a" and char<="z"):
#     print("It is a alphabet")
# else:
#     print ("It is a special character")


#11 WAP to print day name of week.- need to check
# days = input("Enter the week number")
# if days.isweek():
#     print("it is monday")
#     days += 1
# else: 
#     print("it is invalid data")


#12 WAP to accept two integers and check whether they are equal or not. - Done
# Num1 = int(input("enter first number:"))
# Num2 = int(input("Enter second number:"))
# if Num1 == Num2:
#     print("it is equal number:", "i.e", Num1 ,"=" , Num2)
# else:
#     print("it is not equal number", "i.e", Num1 , "!=", Num2)


#13 WAP to determine a candidate's age is eligible for casting the vote or not. - Done
# Age = int(input("Enter the age:"))
# if Age >= 18:
#     print("Can vote because the age is:", Age)
# else:
#     print("Can't vote because the age is:", Age)


#14 WAP to find the eligibility of admission for an engineering course based on the criteria. - Done
# Maths = int(input("Enter the marks:"))
# Physics = int(input("Enter the marks:"))
# Chemistry = int(input("Enter the marks:"))
# Average = int(Maths + Physics + Chemistry)/3
# if Average >= 75:
#     print("Eligible take addmission")
#     if Maths >=75:
#         print("Eligibility becuase qualified category")
#     elif Physics >= 70:
#         print("Eligibility becuase qualified category")
#     else:
#         print("Eligibility becuase qualified category")
# else:
#     print("Not eligible")


#15 WAP to calculate the total marks, percentage and division of students. - Done
# Math = int(input("Enter math's marks:"))
# Physics = int(input("Enter Physics's marks:"))
# Chemistry = int(input("Enter Chemistry's marks:"))
# Total_Marks = (Math + Physics + Chemistry)
# Percentage = (Total_Marks*100/300)
# if Percentage >= 85:
#     print("Division__I ")
# elif Percentage >= 75:
#     print("Division__II")
# elif Percentage >= 65:
#     print("Division__III")
# else:
#     print("Division__IV")


#16 WAP to enter month number and print number of days in month - Done
# Month = int(input("Enter the month Number:"))
# if Month in [1, 3, 5, 7, 8, 10, 12]:
#     print("The number of days is 31")
# elif Month in [4, 6, 9, 11]:
#     print("The number of days is 30")
# else:
#     print("The number of days is either 28 or 29")


#17 WAP to count total number of notes in entered amount.s - Done
# Amount = int(input("Enter the amount:"))
# Notes = int(input("Enter the value of currency:"))
# Num_of_Notes = int(Amount/Notes)
# if Amount / Notes:
#     print("The total amount is:", Amount , "and totla number of notes is:", Num_of_Notes)
# else:
#     print("Can't count")


#18 WAP to check whether a triangle can be formed by the given value for the angles.- Done
# A = int(input("Enter the first number:"))
# B = int(input("Enter the second number:"))
# C = int(input("Enter the third number:"))
# if A+B>C and B+C>A and C+A>B:
#     print("Triangle can be formed")
# else:
#     print("Triangle can't be formed")


#19 WAP to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye"- Done
# Num = int(input("Enter number:"))
# if Num%5 == 0: 
#     print("Hello")
# else:
#     print("bye")


#20 WAP to calculate the electricity bill (Accept number of unit from user) according to the following criteria: - done
#unit                                                                           price
#First 100units                                                                 No Charge
#Next 100 units                                                                 Rs. 5 per unit     
# After 200 units                                                               Rs. 10 per unit
#(For example if input unit is 350 then total bill amount is RS. 2000)
# unit = int(input("Enter the consumed units:"))
# if unit>= 100 and unit<=199:
#     print("The charge per unit is 5. if the consumed electricity is 100 or less then 100. so, the total charge would be:", unit*5)
# elif unit>200:
#     print("The charge per unit 10 if the consumed electricity is more than 200:", unit*10)
# else: 
#     print("No charges")


#21 WAP to display the last digit of a number. - Done
# digit = int(input("Enter number:"))
# print("Last digit of a number:", digit % 10)


#22 WAP to check whether the last digit if a number is divisible by 3 or not - done
# Num = int(input("Enter number:"))
# if Num%3 == 0:
#     print("it is complete divisible by 3")
# else: 
#     print("it is not complete divisible by 3")


#23 WAP to accept percentage from the user and display the grade according to the following criteria:
# Marks                             Grade
# >90                               A
# >80 and <= 90                     B
# >= 60 and <= 80                   C
# below 60                          D
