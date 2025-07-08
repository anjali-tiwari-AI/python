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


#3 WAP to print multiplication table of a given number - done but not able to solve it from while loop
# Number = int(input('Enter number:'))
# for i in range(1, 11):
#     print(i*Number, end = " ")
#     i += 1


#4 WAP to print all natural numbers in reverse order - Done but not able to solve from for loop
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
# Sum = 0
# for i in range(1, N+1):
#     if i%2 == 0:
#         Sum += i
# print("The sum of the even number is:", Sum)



#7 WAP to print sum of odd number between 1 to n - done 
# Num = 100
# Sum = 0
# for i in range(1, Num+1):
#     if i%2 != 0:
#         Sum += i
# print("Total sum of the odd number is:", Sum) 


#8 WAP to swap first and last digit of the number - Done but not able to solve from loop - need to ask 
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



#10 WAP to find first and last digit of any number



#11 WAP to calculate product of digits of a number
#12 WAP to reverse a number using while and for loop
#13 WAP to calculate power using while and for loop
#14 WAP to find factorial of any number
#15 WAP to check whether a number is Armstrong number or not



#16 WAP to find Armstrong numbers between 1 to n
Num = 586
length = len(str(Num))
i = 0
count = Num[i]
for i in Num:.


    Add = count**length
    print(Add)
    count += 1


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


    
