# Reverse the integer - Done
# Int = int(input("Enter the number for whom you needs to reverse the integer:"))
# while Int>0:
#     New = Int%10
#     print(New, end = " ")
#     Int = Int//10


# Integer is Armstrong or not - Need to ask(if else only)
# Arm = int(input("enter the number for which you wants to check if it is armstrong or not:"))
# Len = len(str(Arm))
# Sum = 0
# while Arm>0:
#     Num = (Arm%10)
#     New = Num**Len
#     print(New)
#     Sum = Sum + New
#     Arm = Arm//10
# print("The sum is:", Sum)
# if Sum == Arm:
#     print("Armstrong")
# else:
#     print("No")


# Given number is prime or not
# Num = int(input("Enter the number:"))
# count = 0
# for i in range(1, 999):
#     if Num % i == 0:
#         print(count)
#         count += 1
#         if count>2:
#             print("Final snawer is = No, it is not a prime number", Num)
#         else:
#             print("Final answer is = Yes, it is a prime number", Num)


# Fibonacci series using iteration
# Num = int(input("Enter the number:-"))
# A, B = 0, 1
# C = 0
# N_th_term = int(input("enter the nth term till then you wants to get fibnacci series:-"))
# for i in range(0, Num):
#     C = A + B
#     A = B 
#     B = C
#     print(C)
#     if i >= N_th_term:
#         print("times", i)
#         break
#     else:
#         print("times", i)
#         continue


# 5. Fibonacci series using recursion - Done
# def Fibonacci(Num):
#     A = 0
#     B = 1
#     C = 0
#     for i in range(Num):
#         C = A + B
#         A = B
#         B = C
#         if Num == 0 or Num == 1:
#             return Num
#         else:
#             print(C)
# Fibonacci(8)


# 6. number is palindrome or not using iteration
Num = int(input("Enter the number for whom you wants to check if it is palindrome or not:-"))
Revised = 0
while Num == 0:
    Num1 = Num%10
    Revised = 

    print(Revised)
    Num = Num//10
print("The revised number is:-", Revised)
