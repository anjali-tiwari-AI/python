# ATM Question 

# Username = "Anjali"
# Current_pass = 987
# Current_Balance = int(100000)
# Name = input("Enter your name:-")
# Password = int(input("Enter the password:-"))
# if Password == Current_pass and Name == Username: 
#     Balance = ("Your current balance is:-", Current_Balance)
#     print(Balance)
#     Withdraw = int(input("How much amount needs to withdraw:-"))
#     New_B = Current_Balance - Withdraw
#     New_Balance = ("New balance is:-", New_B)
#     After_withdrawn = ("You have withdrawn", Withdraw , "and your new balance is:-", New_B )
#     print(After_withdrawn)
# else: 
#     if Name == Username:
#         print("Entered Wrong username")

    # exit()

# Username = "Anjali"
# Current_pass = 987
# Current_Balance = int(100000)
# Name = input("Enter your name:-")
# Password = int(input("Enter the password:-"))
# if Password == Current_pass and Name == Username: 
#     Balance = ("Your current balance is:-", Current_Balance)
#     print(Balance)
#     Withdraw = int(input("How much amount you wants to withdraw:-"))
#     if Withdraw>Current_Balance:
#         print("Can't Withdrawn this much amount becuase your withdrawn amount is greater than the current balance i.e.", Current_Balance)
#         exit()
#     New_B = Current_Balance - Withdraw
#     Denomination = ("You have withdrawn", Withdraw)
#     After_withdrawn = print("You have withdrawn", Withdraw , "and your new balance is:-", New_B )
#     if Withdraw == 0:
#         Withdraw500 = Withdraw%500
#         Withdraw200 = Withdraw%200
#         Withdraw100 = Withdraw%100
#         print("500", Withdraw500, 'and 200', Withdraw200 , "and 100", Withdraw100)
#     New_Balance = ("New balance is:-", New_B)
# elif Username == Name:
#     if Current_pass != Password:
#         print("Entered wrong password, please re-enter the password")
#         exit()
# elif Username != Name:
#     print("Entered wrong username, please re-enter the user name")
#     exit()


# Username = "Anjali"
# Password = 987
# Current_balance = 100000
# Name = input("Enter you name:-")
# Enter_Password = int(input("Enter the password:-"))

# if Username == Name and Password != Enter_Password:
#     print("Entered wrong password, please re-enter the correct password")
#     exit()
# elif Username != Name and Password == Enter_Password:
#     print("Entered wrong username please re-enter the correct username")
#     exit()

# if Username == Name and Password == Enter_Password:
#     print("Your current balance is:-", Current_balance)
#     Withdraw = int(input("Enter the amount you wants to withdraw:-"))
#     New_Withdraw = Withdraw
#     if Current_balance > Withdraw:
#         After_Withdraw = Current_balance - Withdraw
#         print("After withdrawing your current balance is:", After_Withdraw)
#     else:
#         print("Your cuurent balance is:", Current_balance , "and you can't withdraw that much amount becuase your withdrawel amount is more than current balance")


# Note_500 = 0
# Note_200 = 0
# Note_100 = 0

# if Withdraw>=Note_500:
#     Note_500 = Withdraw//500
#     print("The 500 withdrawn notes is:", Note_500)
#     Withdraw = Withdraw%500

# if Withdraw>=Note_200:
#     Note_200 = Withdraw//200
#     print("The 200 withdrawn notes is:", Note_200)
#     Withdraw = Withdraw%200

# if Withdraw>Note_100:
#     Note_100 = Withdraw//100
#     print("The 100 withdrawn notes is:", Note_100)
#     Withdraw = Withdraw%100
# else:
#     print("Invalid amount please enter in multiple of 500, 200, 100")
    
# print("Total you have withdrawn", New_Withdraw , "and your new balance is:", After_Withdraw)


# Reverse = int(input('Enter the value of the string:'))
# Rev = 0
# while Reverse > 0:
#     Rev = Rev*10 + Reverse%10
#     print(Rev)
#     Reverse = Reverse//10



# Reverse = input("Enter the value you wants to reverse:- ")
# Rev = " "
# for i in Reverse[ ::-1]:
#     Rev = i
#     print(Rev , end = " ")


# Reverse = int(input("Enter the value you needs to reverse: "))
# Rev = 0
# while Reverse>0:
#     Rev = Rev*10 + Reverse%10
#     Reverse = Reverse//10
# else:
#     print(Rev)


# Armstrong = int(input("Enter the value to check it is armstrong or not:- "))
# Armstrong2 = Armstrong
# Check_Armstrong = Armstrong
# Count = 0
# while Armstrong>0:
#     Arm = Armstrong%10
#     Count += 1
#     Armstrong = Armstrong//10

# Sum_of_Armstrong = 0
# while Armstrong2>0:
#     Last_value = Armstrong2%10
#     Sum = Last_value**3
#     Sum_of_Armstrong = Sum_of_Armstrong + Sum
#     Armstrong2 = Armstrong2//10

# if Sum_of_Armstrong == Check_Armstrong:
#     print("Yes, the entered number is Armstrong becuase original value is:", Check_Armstrong , "and after checking:", Sum_of_Armstrong)
# else:
#     print("No, the entered number is not Armstrong becuase original value is:", Check_Armstrong , "and after checking:", Sum_of_Armstrong)
    
    
# Prime = int(input("Enter the value: "))
# Count = 0
# for i in range(1 , Prime+1):
#     if Prime % i == 0:
#         Count += 1
        
# if Count > 2:
#     print("Entered number is not Prime:", Prime)
# else:
#     print("Entered number is prime:", Prime)


# Fibonacci = int(input("Enter the Fibonacci number: "))
# Fibo_list = []
# Fibo1 = 0
# Fibo2 = 1
# Fibo3 = 0
# for i in range(Fibonacci):
#     Fibo_list.append(Fibo1)
#     Fibo3 = Fibo1 + Fibo2
#     Fibo1 = Fibo2
#     Fibo2 = Fibo3

# print(Fibo_list)


# Palindrome = int(input("Enter the palindrome number: "))


    
    
    
    