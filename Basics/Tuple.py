#Created list then converted into tuple then need to add or remove something after converting into list then again converted into tuple

# L = []
# N = int(input("How many values:- "))
# for i in range(0, N):
#     Val = int(input("Enter the values:- "))
#     L.append(Val)
# print(L)

# T = tuple(L)
# print(type(T))
# print(T)

# NL = list(T)
# print(NL)
# NL[0] = 100
# print(NL)

# T = tuple(NL)
# print(type(T))
# print(T)

#====================================================================================================================================================
# Sum of list, Multiplication of list, Highest value, Second highest, Lowest value, Second lowest
List_Tuple = []
List_Tuple_Numbers = int(input('Enter the number of values:- '))
for i in range(0, List_Tuple_Numbers):
    Values = int(input("Enter the values of the tuple: "))
    List_Tuple.append(Values)


#-----------SUM-------------DONE
# Tuple = tuple(List_Tuple)
# Sum = 0
# for i in Tuple:
#     Sum = Sum + i
# print(Tuple)
# print(type(Tuple))
# print(Sum)


#-------MULTIIPLICATION-------------DONE
# Multi = 1
# Tup = tuple(List_Tuple)
# for i in Tup:
#     Multi = Multi*i

# print(type(Tup))
# print(Tup)
# print(Multi)

#--------Highest value----------------
Highest = 0
Second_highest = 0
Tup = tuple(List_Tuple)
for i in Tup:
    for j in (i+1, Tup):
        if i > j and i > j+1:
            Highest = i
        elif i > j and  


#==============================================================================================================================================

# # #-----Highest and second highest value --------Done
#--------Lowest and second lowest-----------------------Done
#-----------Sum of even and odd, how many even and odd numbers----------Done
#--------------Prime, Not Prime, Number of prime value and not prime value, sum of prime value and not prime value--------
#--------------------------Palindrome-------------------------------NEED TO ASK
#--------------Armstrong---------------------Done 
#-----------Table of the list-----------------DONE
#----------- Factorial ---------------------------------Done
#------------Ascending and descending order --------------Done 
#----------------Reverse the last number and add to new list ------------------------Done