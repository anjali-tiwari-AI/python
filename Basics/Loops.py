# # While loops questions
# Print Number from 1 to 100
# Num = 1
# while Num<=100:
#     print(Num)
#     Num += 1


# Print number from 100 to 1 
# Num = 100
# while Num>= 1:
#     print(Num)
#     Num -= 1


# print the multiplication table of number A
# Table = 10 
# i = 1
# A = 5
# while Table>= i:
#     print(A*i)
#     i += 1


# print the elements of the following list using a loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# List = 10
# Square = 1
# while List>= Square:
#     print(Square*Square)
#     Square += 1 


# Search for a number x in this tuple using loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Tuple = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# X = 36
# i = 0
# while i < len(Tuple):
#     if i == X:
#          print("Found at index:", i)
#          i += 1


#1 WAP to print alphabets from A to Z (ASCII)- for and while - Done
# for i in range(65, 91):
#     print(chr(i), end=" ")
#     i += 1

# num = 97
# while num<=122:
#     print(chr(num), end= " ")
#     num += 1


#2 WAP to print ASCII values of all characters - Done
# for i in range(0, 127):
#     print(chr(i), end = " ")
#     i += 1


#3 WAP to print multiplication table of a given number - done p
# Number = int(input('Enter number:'))
# for i in range(1, 11):
#     print(i*Number, end = " ")
#     i += 1
#----------or ------------
# Number = int(input("Enter number:"))
# Num = 1
# while Num<=10:
#     print(Number*Num, end = " ")
#     Num +=1 

#4 WAP to print all natural numbers in reverse order - Done 
# Number = int(input("Enter number:"))
# while Number>=1:
#     print(Number, end = " ")
#     Number -= 1


#5 WAP to print sum of digits enter by user
# Num = 7
# Sum = 0
# i = 1
# while i<= Num:
#     Sum += i
#     i += 1
# print('Total Sum:', Sum)

# N = 20
# Sum = 0
# for i in range(1, N+1):
#     Sum += i
# print("Total sum:", Sum)


#6 WAP to find sum of even number between 1 to n - Done not able to solve from while
# N = 20
# Sum = 1
# for i in range(1, N+1):
#     if i%2 == 0:
#         Sum += i
# print("The sum of the even number is:", Sum)
# --------------or -------------------
# Num = int(input("Enter number:"))
# i = 1
# Sum = 0
# while i<=Num:
#     if i%2 == 0:
#         print("The sum of the even number is:", i , "and the total sum is:", Sum)
#     Sum += i
#     i += 1
# print("The sum of all the even number is:", Sum)


#7 WAP to print sum of odd number between 1 to n - done 
# Num = 100
# Sum = 0
# for i in range(1, Num+1):
#     if i%2 != 0:
#         Sum += i
# print("Total sum of the odd number is:", Sum) 


#8 WAP to swap first and last digit of the number - Done 
# Number = 123256938
# count = 0
# A = Number%10
# print(A)
# while Number//10 !=0:
#     Number = Number//10
#     count += 1
# print("The swap number is:", Number)
# print(A, Number)


# Number = 569256
# Swap1 = Number//100
# Swap2 = (Number//1)%10
# print(Swap2, Swap1)


# while Number//10:
#     print(Number)
#     Number//= 10
# print ("The number is:", Number)

# count = 0  #Number of digits
# Number = 125693
# while Number != 0:
#     Number = Number//10
#     print(Number)
#     count += 1
# if Number%count == 0:
#     print("yes the number is divisible by number of digits in that number")
# else:
#     print("no")


#9 WAP to find the sum of first and last digit of any number - Done - but need to check
# Number = 5632
# Sum = 0
# A = Number%10 
# while Number//10 != 0:
#     Number = Number//10
#     Sum += 1
# print(Number+A)


# 10 WAP to find first and last digit of any number
# Num = int(input('Enter number:'))
# Num1 = Num%10
# i = 1
# while Num//10 != 0:
#     Num = Num//10
#     i += 1
# print("The first digit is:", Num , "and the last digit is:", Num1)


#11 WAP to calculate product of digits of a number - Done
# Num = int(input("Enter number:"))
# Digit = 1
# while Num>0:
#     Digit = Digit*(Num%10)
#     print(Digit)
#     Num = Num//10
# print("The multiplication of the number is:", Digit)



#12 WAP to reverse a number using while and for loop - Done
# Num = int(input('Enter number:'))
# i = 0
# while Num>1:
#     i = Num%10
#     print(i, end = " ")
    # Num = Num//10
# -------for loop----- (Need to ask)
# Num = int(input("Enter number:"))
# for i in range(1, len(Num)):
#     Num = Num%10
#     print(Num)
#     i += 1


#13 WAP to calculate power using while and for loop
# Num = int(input("Enter number:"))
# Power = int(input("Enter number:"))
# i = 1
# R = 1
# while i<=Power:
#     R = Num*R
#     print(R)
#     i += 1
# print("The power of the number is:", R)

# #14 WAP to find factorial of any number - Done
# X = int(input('Enter number:'))
# i = 1
# R = 1
# while i <= X:
#     R = R*i
#     print(R)
#     i += 1
# print("The factorial of the number", X, "is", R)

#15 WAP to check whether a number is Armstrong number or not



#16 WAP to find Armstrong numbers between 1 to n
# Num = 586
# length = len(str(Num))
# i = 0
# count = Num[i]
# for i in Num:.


#     Add = count**length
#     print(Add)
#     count += 1


#17 WAP to calculate compound interest - Done
# P = int(input("Enter principle amount:"))
# R = float(input("Enter rate:"))
# T = int(input("Enter time duration:"))
# i = 0
# for i in range(T):
#     Amount = P*(1+(R/100))**T
#     CI = Amount - P
#     print("The compound interest is:", CI)
#     i += 1
# print("The compound interest is:", CI)


#18 WAP to check a enter number is prime number or not using while and for loop - Done
# Num = int(input("Enter number:"))
# count = 0
# i = 1
# while i<=Num:
#     if Num%i==0:
#         count = count+1
#     i += 1
# if count==2:
#     print("Yes, it is a prime number")
# else:
#     print("it is composite number")

# By for loop
# Num = int(input("Enter number:"))
# count = 0
# for i in range(2, Num+1):
#     if Num%i==0:
#         print(Num, "is divisible by:", i)
#         count = count + 1
#     i += 1
# if count == 1:
#     print("Yes it is a prime number:", Num)
# else:
#     print("No, it is a composite number:", Num)
          


#19 WAP to check whether a number is palindrome or not - Done but Need to ask about changing i and num
# Num = int(input('Enter Number:'))
# i = Num
# Reverse = 0
# while Num>0:
#     Reverse = (Reverse*10) + Num%10
#     Num = Num//10
# if i == Reverse:
#     print("yes")
# else:
#     print("no")


#20 WAP to print number in words - Ask
# Words = "I love myself"
# idx = 0
# for i in Words:
#     print(i, end = " ")
#     idx += 1 


#21 WAP to find HCF of two numbers
# N1 = int(input("Enter first number:"))
# N2 = int(input("Enter second number:"))
# if N1>N2:
#     Div = N1
#     HCF = N2
# else:
#     Div = N2
#     HCF = N1
# Remainder = Div%HCF
# while Remainder != 0:
#     Div = HCF
#     HCF = Remainder
#     Remainder = Div%HCF
# LCM = (N1 * N2) /HCF
# print("The LCM is:", LCM , "and", "The HCF is:", HCF)


#22 WAP to find LCM of two numbers
# A = int(input("Enter first number:"))
# B = int(input("Enter second number:"))
# Max_num = max(A, B)
# while True:
#     if Max_num%A == 0 and Max_num%B == 0:
#         print(Max_num)
#         break
# print("The LCM of the both number is:", Max_num)


    
# 1 - Check if All Digits of a Number Are the Same - Done
# e.g. 1111 → True, 1234 → False
# Num1 = 8963
# Num2 = 4563
# i = 0
# while i>=Num1:
#     Num1 = Num1%10
#     print(Num1)
#     Num1 = Num1//10
# if Num1==Num2:
#     print("Yes, it is same")
# else:
#     print("No, it is not same")


# 2-Count the Number of Times a Digit Appears in All Numbers From 1 to n - Done - but it is not a profesional coding 
# Num = 989
# count = 0
# Number = 9
# while Num > 0:
#     Num1 = Num%10
#     print(Num1)
#     if Num1 == Number:
#         print("The number of times the digits appeared is:", count)
#     else:
#         print("No")
#     count += 1
#     Num = Num//10
    


# 3-Check if the Digits of a Number Are in Increasing Order - not able to solve
# Num = 123867
# Previous = 10
# result = True
# while Num>0:
#     current = Num%10
#     print(current)
#     if Previous < current:
#         result = False
#         break
#     Previous = current
#     Num = Num//10




# 4-Reverse the Digits of a Number Only If It's a Palindrome - Done but need to ask about if becuase it is showing wrong result
# Num = int(input("Enter number:"))
# Rev = 0
# while Num>0:
#     Rev = (Rev*10) + Num%10
#     Num = Num//10
#     print(Rev)
#     if Num == Rev:
#         print(Rev)
#     else:
#         print("No")
        
    

# 5-Find the Smallest Number With a Given Digit Sum








# 6-Count How Many Times You Need to Multiply Digits Until You Reach a Single Digit 
# (Multiplicative Persistence) - Need to check 
# Num = int(input("Enter number:"))
# count = 0
# while Num != 0:
#     D = 1
#     Rem = Num%10
#     D = Rem*D
#     count += 1
#     print(D)
#     Num = Num//10
#     Num = Num*D
#     if D<10:
#         print("Single", D)

# Num = 89
# i = 1
# count = 0
# while Num != 0:
#     count += 1
#     Rem = Num%10
#     i = Rem*Num
#     Num = Num//10
#     i += 1
#     if i<10:
#         print(count)
#         print(i)
#         break 
#     Num = i


# 7-Find the Largest Digit in a Number - need to ask
# Num = int(63963)
# i = 1
# while Num>0:
#     Rem = Num%10
#     print(Rem)
#     Num = Num//10
#     if Rem >= 9:
#         print("The largest number is:", Rem)
#     elif Rem > 8:
#         print("The largest number is:", Rem)
#     elif Rem >= 7:
#         print("The largest number is:", Rem)
#     elif Rem > 6:
#         print("The largest number is:", Rem)
#     elif Rem == 5:
#         print("The largest number is:", Rem)
#     elif Rem == 4:
#         print("The largest number is:", Rem)
#     elif Rem == 3:
#         print("The largest number is:", Rem)
#     elif Rem == 2:
#         print("The largest number is:", Rem)
#     else:
#         print("The largest number is:", Rem)


# 8-Print All Numbers Between 1 and 1000 Whose Sum of Digits Is a Prime


# 9-Create a Program to Detect a "Mountain" in a List

# 10-Print All Pairs (i, j) From 1 to 100 Where i * j Ends with 9


# 11-Count How Many Prime Numbers Are Palindromes Between 1 and 1000




# 12-Generate the First 10 Numbers Where the Number Equals the Sum of the Factorials of Its Digits - Check
# for i in range(1001):
#     Num = i
#     print(i)
#     Fact = 1
#     J = 1
#     while J<=Num:
#         Fact *= J
        
#         J += 1
#         print("Total sum:", Fact)


# 13-Given a Number, Rearrange Its Digits to Form the Largest Possible Number - did get ans need to increase
# Num = 45963
# count = 1
# while Num != 0:
#     Num1 = Num%10
#     print(Num1)
#     Num = Num//10
#     print("The number of times the digits appeared in number:", count)
#     count += 1
#     print()


# 14-Print All Numbers from 1 to 100 That Contain No Repeated Digits - Need to check
# for i in range(1, 101):
#     Num = i
#     print(i)
#     while i>0:

#------------------Pattern--------------------------------

# * * * * * *
# * * * * *
# * * *
# * *
# *

# r = 5
# for i in range(r , 0, -1):
#     for j in range(i):
#         print("*", end = " ")
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# A = 7
# for i in range(1 , A+1):
#     for i in range(1 , i):
#         print("*", end = " " ,)
#     print()


#           *
#         * *
#       * * *  
#     * * * *
#   * * * * * 
# * * * * * *
# T = 6
# for i in range(1, T, 1):
#     for j in range(i):
#         print(j)
#     print()


# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
