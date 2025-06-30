#--------------------------------------------Booklet questions---------------------------------------------------------------
#1 WAP to reverse an integer in python
# Value = 5694
# Ones = (Value//1)%10 #4 
# Ten = (Value//10)%10
# Hundred = (Value//100)%10
# Thousand = (Value//1000)%10
# print("Ones Number is:", Ones)
# print("Ten Number is:", Ten)
# print("Hundred Number is:", Hundred)
# print("Thousand Number is:", Thousand)
# Reverse_Number = Ones*1000 + Ten*100 + Hundred*10 + Thousand*1


#2 WAP to check whether an integer is Armstrong number or not.
# Num1 = 153
# Num2 = 56959
# Arm = 1**3 + 5**3 + 3**3
# Arm1 = 5**5 + 6**5 + 9**5 + 5**5 + 9**5
# print(Arm)
# print(Arm1)
# if Num1 == Arm:
#     print("True")
# else:
#     print("False")


#3 WAP to check given number is prime or not.(Which is divisible either by its own number or 1) - Need to see again
# Number = int(input("Enter the number:"))
# if Number%2 ==0:
#     print("No")
# else:
#     print("Yes")

# if Number//1 == Number and Number//Number == 1 and Number%2 == 0:
#     print("No")
# else:
#     print("Yes")

# Number = input("Enter the number:")
# Num = 1
# for i in range(int(2, Number)):
#     if (Number %= 0):
#         Num = True
#         break

# if Num:
#     print("prime")
# else:
#     print("no")

# for i in range(1, Number):
#     if Number %i == 0:
#         print("prime")
#     else:
#         print("not a prime number")

# # if Number >= 1:
# for i in range (1, Number):
#     if Number%i == 0:
#         print("it is a prime number")
#     else: 
#         print("It is not a prime number")


#4 WAP to print the fibonacci series using iteration -- need to check again
# fibonacci_series = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# List = [4, 8, 6, 7, 3, 9]
# # R = List[0]
# # R1 = len(List)
# # for i in range(R1):
# #     print(List[i])
# #     R += List[i]

# R = List[0]
# R1 = len(List)
# for i in range(R1):
#     print(List[i])
#     i += List[i]
   
    
# i = List[0]
# if i <= List[i]:
#     for i in range(List[0], List[8]):
#         print(i)
#         i+= List[i]

# i = List[i]
# if i<= List[i]:
#     for i in range(List[0], List[i+1]):
#         print(i)
#         i += List[i]
        

#5 WAP to print the Febonacci series using recursion
Febonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


#6 WAP to check whether a number is palindrome or not using iteration #we can print through indexing - [121, 1331, 14541, 8998] - check
# pal = 1221
# V1 = int(pal/1)%10
# V2 = int(pal/10)%10
# V3 = int(pal/100)%10
# V4 = int(pal/1000)%10
# print(V4, V3, V2, V1)
# or



#7 WAP to check whether a number is palindrome or not using recursion



#8 WAP to find greatest among three integers - if first integer is 9 and last integer is 9 then it is highest 
# or first integer is less than 9 and last integer is 9 then it is highest
list = [56, 89, 25]




#9 WAP to check if a number is binary - [1 , 0]

#10 WAP to find sum of digits of a number using recursion
#11 WAP to swap two numbers without using third Variable - check again
# A = 25 #16
# B = 16 #25
# B = A
# A = A + B #41

# print(A , B)


#12 WAP to swap two numbers using third Variable - done
# A = 5
# B = 8
# A , B = B, A
# print(A , B)


#13 WAP to find prime factors of a given integer - only complete divisible by its own number only
prime = [7, 19, 45, 29, 63, 47, 52, 53, 89]
i = prime[]
while i in prime:
    print(prime[i])
    i += 1



#14 WAP to add two integer without using arithmetic + Operator - Ans 13 - Need to check




# or
# A = B - A #3
# B = B//5
# A = A*A
# B = A//B
# print(A , B)

#15 WAP to check given number is perfect or not
# Num = int(input("Enter the number:"))
# n = 2
# for i in range():
#     if i%n == 0:
#         n += 1


# Num = int(input("Enter the number:"))
# sum = 0
# n= 2
# def Perfect_number(a):
#     Fact1 = a%n == 0
#     n += 1
#     sum = Fact1 + n
#     print("it is a perfect number")
    
        

#16 WAP to find the average of number with explanations -- Done
# def avg_num(a , b, c):
#     sum = a + b + c
#     print(sum)
#     Avg = sum/3
#     print(Avg)
#     return Avg
# avg_num(8 , 7 , 6)


# Num = int(input("Enter the numbers:"))
# Avg = 3
# i = 8
# while i :
#     Num[0]


#17 WAP to calculate factorial using iterative method
#18 WAP to calculate factorial using recursion



#19 WAP to check given number is even or odd -- Done
# Num = 16
# if Num%2 == 0:
#     print("Even")
# else: 
#     print("odd")

#20 WAP to print first n prime number with explanation
#21 WAP to print prime number in a given range 
#22 WAP to find smallest number among three



#23 WAP to calculate the power using the POW mathod -- Done
# import math
# Num = 5
# por = 3
# x = pow(Num, por)
# print(x)


#24 WAP to calculate the power without using POW function - Done
# Base_No = 5
# Power_No = 3
# Result = Base_No**Power_No
# print(Result)


#25 WAP to calculate the square of the given number - Done
# Number = 7
# print(Number**2)


#26 WAP to calculate the cube of the given number - Done
# Number = 2
# cbe = 3
# Cube = Number**cbe
# print(Cube)


#27 WAP to calculate the square root of the given number - Done 
# import math
# Number = 11
# Square_root = math.sqrt(Number)
# print(Square_root)

#28 WAP to calculate the LCM of the given two number - need to check again
# Num1 = 151
# Num2 = 76
# LCM = (Num1 and Num2)%2 == 0
# print(LCM)

#29 WAP to find GCD (Greatest common diviser) or HCF of two number
#30 WAP to find GCD of two numbers using recursion
#31 WAP to convert decimal number into binary
#32 WAP to convert decimal number to octal number


#33 WAP to check the given year is aleap year or not -- done 
# Leap_Year = [2000, 2004, 2008, 2012, 2016, 2020] or (2000+4)
# Year = int(input("Enter the year:"))
# if Year%4 == 0:
#     print("It is a leap year")
# else: 
#     print("It is not a leap year")

#34 WAP to convert celsius to fahrenheit
#35 WAP to convert Fahrenheit to Celsius

#36 WAP to calculate simple interest with explanation - done 
# Principle = 5000
# Rate = 7
# Time = 12
# Simple_Interest = (Principle * Rate * Time)/100
# print(Simple_Interest)
    

    
