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


#4 WAP to find the largest among three variables using nesting if. - Done
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

#==============================ASCII=============================================================
# asc = input("Enter:")
# print(chr(asc))
# ord() -> character_to_Ascii
# chr()-> ASCII to character

#---------------------------------------------------------------------
#9 WAP to check entered character vowel or consonant. - Done
# char = input("Enter the character:")
# if (char =="A" or char=="E" or char=="I" or char=="O" or char=="U" or char=="a" or char=="e" or char=="i" or char=="o" or char=="u"):
#     print("it is Vowel")
# else:
#     print("it is a consonant")
# ----------------------or ------------------------------------------
# char = input("Enter the character:")
# Vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
# if char in Vowels:
#     print("it is Vowels")
# else:
#     print("it is a consonant")


#10 WAP to check whether a character is alphabet, digit or special character. - Done 
# x = input("Enter the data:")
# if (ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122):
#     print("it is alphabate")
# elif ord(x)>=48 and ord(x)<=57:
#     print("it is integer")
# else:
#     print("it is special character")
    

#11 WAP to print day name of week.- Done
# days = int(input("Enter the week number:-"))
# if days == 1:
#     print("Today is Monday")
# elif days == 2:
#     print("Today is Tuesday")
# elif days == 3:
#     print("Today is Wednesday")
# elif days == 4:
#     print("Today is Thursday")
# elif days == 5:
#     print("Today is Friday")
# elif days == 6:
#     print("Today is Saturday")
# elif days == 7:
#     print("Today is Sunday")
# else:
#     print("Input data is invalid")



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


#23 WAP to accept percentage from the user and display the grade according to the following criteria: - Done
# Marks                             Grade
# >90                               A
# >80 and <= 90                     B
# >= 60 and <= 80                   C
# below 60                          D
# Marks = int(input("Enter the obtain marks:"))
# if Marks >90:
#     print("The grade is:A because the marks is:", Marks)
# elif Marks >80 and Marks <= 90:
#     print("The grade is:B because the marks is:", Marks) 
# elif Marks >= 60 and Marks <= 80:
#     print("The grade is:C because the marks is:", Marks)
# else:
#     print("The grade is:D because the marks is:", Marks)


#24 WAP to accept the cost price of a bike and display the road tax to be paid according to the following criteria: - Done
# Cost price(in Rs.)                    Tax 
# >100000                               15%
# >50000 and <= 100000                  10%
# <= 50000                              5%
# Cost_price = int(input("Enter the cost price of a bike:"))
# if Cost_price > 100000:
#     print("The cost price would be 15% i.e. in amount it would be:", Cost_price*15/100, "total amoount paid")
# elif Cost_price > 50000 and Cost_price <= 100000:
#     print("The cost price would be 10% i.e. in amount it would be:", Cost_price*10/100, "total amoount paid")
# else:
#     print("The cost price would be 5% i.e. in amount it would be:", Cost_price*5/100, "total amoount paid")


#26 WAP to accept a number from 1 to 12 and display name of the month and days in the month like 1 for january and number of days 30 
# Month = int(input("Enter the number of the month:-"))
# if Month == 1:
#     print("The month is January and the number of days is 31")
# elif Month ==2:
#     print("The month is February and the number of days is 28/29")
# elif Month ==3:
#     print("The month is March and the number of days is 31")
# elif Month ==4:
#     print("The month is April and the number of days is 30")
# elif Month ==5:
#     print("The month is May and the number of days is 31")
# elif Month ==6:
#     print("The month is June and the number of days is 30")
# elif Month ==7:
#     print("The month is July and the number of days is 31")
# elif Month ==8:
#     print("The month is August and the number of days is 31")
# elif Month ==9:
#     print("The month is September and the number of days is 30")
# elif Month ==10:
#     print("The month is October and the number of days is 31")
# elif Month ==11:
#     print("The month is November and the number of days is 30")
# elif Month ==12:
#     print("The month is December and the number of days is 31")
# else:
#     print("Enter data is invalid")


#27 WAP to accept any city from the user and display monument of that city - Need to check 
# City              Monument
# Delhi             Red Fort 
# Agra              Taj Mahal
# Jaipur            Jal Mahal
# city = input("Enter city name:")
# city = "Monument"
# city = "Delhi" == "Red Fort"
# city = Agra = "Taj Mahal"
# city = Jaipur = "Jal Mahal"
# print("The Monument name of the city is:", city)


#27 WAP to check whether a number entered is three digit number or not: - Need to check 
# Num = int(input("Enter Number:-"))
# Num1 = Num//100
# if Num1//10:
#     print("it is a 3 digit number")
# else:
#     print("it is not 3 digit number")



# if Number//100:
#     print("it is a 3 digit number")
# else:
#     print("it is not a 3 digit number")

# Number = int(input("Enter number:"))
# if Number == int(Number[0], Number[1], Number[2]):
#     print("it is a 3 digit number")
# else:
#     print("it is not a 3 digit number")


#WAP to check whether a person is senior citizen or not. - Done
# Senior = int(input('Enter the age of the person:'))
# if Senior>=60:
#     print("Yes, This person comes in the senior citizen list")
# else:
#     print("No, This person doesn't comes in the senior citizen list")


# WAP to find the lowest number out of the two numbers excepted from user. - Done
# Num1 = int(input("Enter first number:"))
# Num2 = int(input("Enter second number:"))
# if Num1>Num2:
#     print("Num2 is the lowest number")
# elif Num1<Num2:
#     print("Num1 is the lowest number")
# else:
#     print("Both number are equal")


# WAP to find the Largest number out of the two numbers excepted from user. - Done
# Num1 = int(input("Enter first number:"))
# Num2 = int(input("Enter second number:"))
# if Num1>Num2:
#     print("Num1 is the Largest number")
# elif Num1<Num2:
#     print("Num2 is the Largest number")
# else:
#     print("Both number are equal")


# WAP to check whether a number (accepted from user) is positive or negative
# Num = int(input("Enter first number:"))
# if Num >= 1:
#     print("it is a positive number")
# else:
#     print("it is a negative number")


# WAP to check whether a number (Accepted from user) is divisible by 2 and 3 both:- Done
# Num = int(input("Enter number:"))
# if Num%2==0 and Num%3==0:
#     print("Yes", Num, ", this number is divisible from both 2 and 3")
# else:
#     print("No", Num, ", it is not divisible from 2 and 3")


# WAP to find the largest number out of three number excepted from user - Done
# Num1 = int(input("Enter first number:"))
# Num2 = int(input("Enter second number:"))
# Num3 = int(input("Enter third number:"))
# if Num1>Num2 and Num1>Num3:
#     print("Num1 is the greatest number i.e.:", Num1)
# elif Num2>Num3:
#     print("Num2 is the greatest number i.e:", Num2) 
# else:
#     print("Num3 is the greatest number", Num3)


# Accept the temperature in degree celsius of water and check whether it is boiling or not(Boiling point of water in 100* C) - Done
# Temp_Water = int(input("Temperature in degree celsius of water:"))
# if Temp_Water>= 100:
#     print("The water is Boiling")
# else:
#     print("The water is not Boiling")


# Accept the age of 4 persons and display the youngest one?
# Person1 = int(input("Enter the age of the first person:-"))
# Person2 = int(input("Enter the age of the second person:-"))
# Person3 = int(input("Enter the age of the third person:-"))
# Person4 = int(input("Enter the age of the fourth person:-"))
# if Person1<Person2 and Person1<Person3 and Person1<Person4:
#     print("Person1 is the youngest person")
# elif Person2<Person3 and Person2<Person4 and Person2<Person1:
#     print("Person2 is the youngest person")
# elif Person3<Person1 and Person3<Person2 and Person3<Person4:
#     print("Person3 is the youngest person")
# else:
#     print("Person4 is the youngest person")


# WAP to check whether a number is prime or not

