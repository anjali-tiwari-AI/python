# WAP in python, In list 1 - 100 numbers are stored, one number is missing how do you find it.
# list = [1, 5, 8, 11, 23, 35, 49, 56, 68, 73, 82, 91]
# for i in range(1, 101):
#     if not i in list:
#         print(i, end = " , ")

# 2. WAP in python for, in a list(array) 1 - 100 multiple numbers are duplicates, how do you find it
# List = [1, 2 , 3 , 4 , 5, 6 , 7 , 8, 9 , 10 , 11, 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 
#         22 , 23 ,24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35, 36 , 37 , 38 , 39 , 40 , 
#         41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49, 50 , 51 , 52 , 53 , 54 , 55 , 56, 57 , 58 , 59 , 
#         60 , 61 , 62 , 63 , 64 , 65 , 66 , 67 , 68, 69 , 70 , 71 , 72 , 73, 74 , 75 , 76 , 77 , 78 , 
#         79 , 80 , 81 , 82, 83 , 84 , 85 , 86 , 87 , 88 , 89 , 90 , 91, 92 , 93 , 94 , 95 , 96 , 63 ,
#         97 , 98 , 99 , 100 , 58, 53, 46, 75, 86, 21, 4, 9, 63, 75, 26, 45, 9, 3, 46, 51, 86, 29, 95 , 
#         75, 46, 42, 19, 28, 43, 85, 42, 42, 22, 16, 19, 11, 22, 33, 44, 88, 66, 77, 88]

# i = 0
# unique = []
# Duplicate = []
# for element in List:
#     if element not in unique:
#         unique.append(element)
#     elif element not in Duplicate:
#         Duplicate.append(element)
# print("The unique value:", unique)
# print("The duplicate value is:", Duplicate)


# 3. WAP in python to find first duplicate numbers in a given list(array) -- Done
# List = [10, 5, 8, 3, 1, 9, 4, 5, 6, 7, 2, 6, 4]
# count = 1
# Duplicate = []
# Unique = []
# Duplicate_first = []
# for element in List:
#         if element not in Unique:
#                 Unique.append(element)
#         elif element not in Duplicate:
#                 Duplicate.append(element)
#                 if element in Duplicate and Unique:
#                      Duplicate_first.append(element)
#                      count = 1
#                      break   
# print("Dup:", Duplicate)
# print("unique:", Unique)
# print("Duplicate_first:", Duplicate_first)


# 4. WAP in python to remove duplicate elements from array(list) - Done
# List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 5, 7, 9, 3, 4, 6, 1, 8, 8, 6, 6, 7, 3, 4, 9]
# unique = []
# duplicate = []
# for element in List:
#     if element not in unique:
#         unique.append(element)
#     elif element not in duplicate:
#         duplicate.append(element)
# print("unique =", unique)
# print("Duplicate:", duplicate)


# 5. WAP in python for, given two arrays 1, 2, 3, 4, 5 and 2, 3, 1, 0, 5 
# and find which number is not present in the second array. --- Need to check
# List1 = [1, 2, 3, 4, 5]
# List2 = [2, 3, 1, 0, 5]
# Not_present = []
# NP = []
# i = 0
# for element in List1 and List2:
#     if element in List1 and not List2:
#         print(element)
#     elif element in List2 and not List1:
#         print(element)


# 6. WAP in python for, how to compare two array is equal in size or not. -- not able to solve
# Array1 = [1, 2, 3, 4, 5]
# Array2 = [1, 2, 4, 1, 4]
# A  = Array1.sort()
# B = Array2.sort()
# if A == B:
#     print(True)
# else:
#     print(False)
# print(A) 
# print(B)


# for element in Array1 and Array2:
#     if len(Array1) == len(Array2):
#         print("Yes, it is equal")
#         break
#     else:
#         print("No, it is not equal")
#         break


# 7.1. WAP in python, to find smallest number in array. - Done
# A = [] # 5, 9, 2, 4, 6, 3, 7
# Size = int(input("Enter the size of the list:"))
# for i in range(Size):
#     Value = int(input("Enter number:"))
#     A.append(Value)
# Minimum = A[0]
# for i in range(Size):
#     if A[i]<Minimum:
#         Minimum = A[i]  
# print("Minimum value is:", Minimum) 


# 7.2. WAP in python, to find largest number in array. - Done
# Num = [45, 86, 26, 91, 13, 7]
# Largest = Num[0]
# for i in range(len(Num)):
#     if Num[i]>Largest:
#         Largest = Num[i]
# print(Largest)


# A = []
# Size = int(input("Enter the size of the number:"))
# for i in range(Size):
#     Value = int(input("Enter the number:"))
#     A.append(Value)
# Maximum = A[0]
# for i in range(Size):
#     if A[i]>Maximum:
#         Maximum = A[i]
# print("The all numbers is:", A)
# print("The maximum number is:", Maximum)        


# 8 WAP in python, to find second highest number in an array - Done
# Size = int(input("Enter the elements(Size of the number:"))
# Nums = []
# for i in range(Size):
#     Num = int(input("Enter the numbers:"))
#     Nums.append(Num)
# Largest = Nums[0]
# Sec_largest = Nums[0]
# for i in range(len(Nums)):
#     if Nums[i]>Largest:
#         Largest = Nums[i]
# for i in range(len(Nums)):
#     if Sec_largest<Nums[i] and Nums[i] != Largest:
#         Sec_largest = Nums[i]
# print(Sec_largest)


# Number = [12, 25, 75, 36, 39, 81, 43, 61, 95, 72, 53]
# Largest = Number[1]
# Sec_Largest = Number[0]
# for i in Number:
#     if Number>Largest:
#         Largest = Number
#         Sec_Largest = Largest
#         Largest += 1
#         Sec_Largest += 1
#         print("Largest:", Largest , "snd second largest:", Sec_Largest)
#     elif Number>Sec_Largest and Number<Largest:
#         Sec_Largest = Number
#         print("Largest:", Largest , "snd second largest:", Sec_Largest)
#         Largest += 1
#         Sec_Largest += 1

# A = []
# Size = int(input("The size of the number is:"))
# for i in range(Size):
#     Value = int(input("Enter the number:"))
#     A.append(Value)
# Highest = A[0]
# Sec_high = A[1]
# High2 = Sec_high[0]
# for i in range(Size):
#     if A[i]>Highest:
#         print("The highest number is:", A[i])
#         Sec_high.append(A[i])
#         Highest = A[i]
#         if Sec_high>High2:
#             print("The second highest number is:", Sec_high)      
# print("The highest number is:", Highest)
# print("The second highest number is:", High2)


# 9 WAP in python, to find top two maximum number in an array - Done
# Array = [42, 75, 34, 98, 23, 10, 46, 37]
# Max1 = Array[0]
# Max2 = Array[0]
# for i in range(len(Array)):
#     if Array[i]>Max1:
#         Max1 = Array[i]
#         print("Max1:", Max1)
#         for i in range(len(Array)):
#             if Max1>Array[i] and Array[i]>Max2:
#                 Max2 = Array[i]
#                 print("Max2:", Max2)
# print("The largest first and second maximum number is:", Max1 , "and", Max2)


# 10 WAP to print array in reverse order - [Starting:Ending:step(increment or decrement)] - Done
# List = [45, 36, 76, 96, 82, 23, 56, 61]
# # print(List[-1::-1])
# ---- or ----
# List.reverse()
# print(List)
# # ------or----
# for i in range((len(List)-1), -1, -1):
#     print(List[i], end = " ")


# 11 WAP to reverse an array in two ways - didn't understand the question



# 12 WAP to calculate length on an array
# Value = [75, 96, 25, 36, 46]
# count = 0
# for i in Value:
#     count += 1
# print(count)


# 13 WAP to insert an element at the end of an array
# Array = [42, 85, 36, 61, 52, 29, 75, 94, 16]
# Array.append(789)
# print(Array)


# 14 WAP to insert element at a given location in array - List.insert(index,value) - Need to check
# List = [45, 63, 85, 72, 15]
# Value = 100
# Position = 2
# List.append(None)
# for i in range(len(List)):
#     List[i+1] = List[i]
# List[Position-1] = Value
# print(List)


# A = []
# Size = int(input("Enter the size of the A:"))
# for i in range (Size):
#     Value = int(input("Enter the elements:"))
# Pos = int(input("Enter the position where the element needs to put:"))
# Key = int(input("Enetr the number which needs to add in A:"))
# A.append(None)
# print(A)
# for i in range(Size-1, Pos-2, -1):
#     A[i+1]=A[i]
# A[Pos-1] = Key
# print(A)



# ---------or -------
# List = [75, 25, 43, 16, 67, 82, 92]
# List.insert(2, 100)
# print(List)


# 15 WAP to delete element at end of array - use pop to delete - Done

# ----or-------
# List = [56, 75, 25, 36]
# List.pop(2)
# print(List)


# 16 WAP to delete given element from array - Done
# A = []
# Size = int(input('Enter the size of the A:'))
# Flag = 0
# for i in range(Size):
#     Value = int(input("Enter the numbers:"))
#     A.append(Value)
# print("Original list is:", A)
# Key = int(input("Enter the Number which needs to find for deletion:"))
# for i in range(Size):
#     if A[i] == Key:
#         Flag = 1
#         Pos = i
#         break
# if Flag == 0:
#     print("Element not found")
# else:
#     for i in range(Pos, Size-1):
#         A[i] = A[i+1]
#         A.pop()
#         print("Final list after delete the element:", A)


# 17 WAP to delete element from array from given index
# List = [12, 34, 56, 78, 90]
# index = 2
# List.pop(index)
# print(List)
#---or----
# del List[index]
# print(List)

# ----or -----
# A = []
# Size = int(input("Enter the size of A:"))
# Index = int(input("Enter th index number which needs to delete:"))
# Flag = 0
# for i in range(Size):
#     Value = int(input("Enter the numbers:"))
#     A.append(Value)
# for i in range(Size):
#     if i == Index:
#         Flag = 1
#         Position = i
#         break
# for i in range(Size):
#     if Flag == 0:
#         print("Index not found")
#     else:
#         for i in range (Position, Size-1):
#             A.pop(Index)
# print("The list after delete the index", A)


# 18 WAP to find sum of array elements. - Done
# List = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# Sum = 0
# index = 1
# for i in List:
#     Sum = i+Sum
#     print(Sum)
# print("The total sum is:", Sum)


# 19 WAP to print all even numbers in array - Done
# List = [45, 25, 26, 76, 23, 94, 81, 46, 10, 28, 37]
# for i in List:
#     if i%2 == 0:
#         print(i, end = " ")


# 20 WAP to print all odd numbers in array - Done
# Odd = [45, 76, 25, 86, 94, 20, 13, 75, 48, 29]
# for i in Odd:
#     if i%2 != 0:
#         print(i , end = " ")


# 21 WAP to perform left rotation of array elements by two positions - Done
# A = []
# Size = int(input("Enter the size of the A:"))
# for i in range(Size):
#     Value = int(input("Enter the elements for A:"))
#     A.append(Value)
# print("The original list is:", A)
# Key = A[0]
# Key_2 = A[1]
# for i in range(1, Size):
#     A[i-1] = A[i]
# for i in range(0, Size):
#     A[i-1] = A[i]
# A[Size-1] = Key
# A[Size-2] = Key_2
# print("After modification the list would be:", A)



# 22 WAP to perform right rotation in array by 2 positions - Done
# A = []
# Size = int(input("Enter the size of the A:"))
# for i in range(Size):
#     Value = int(input("Enter the number of the value:"))
#     A.append(Value)
# Key = A[Size-1] 
# Key_1 = A[Size-2]
# print("The original list is:", A)
# for i in range(Size-3, -1, -1): #start, stop, step
#     A[i+2] = A[i]
# A[0] = Key
# A[1] = Key_1
# print("After modification the list is:", A)


# 23 WAP to merge two array - Done
# Array1 = [12, 32, 45, 36, 55, 66]
# Array2 = [75, 89, 95, 46, 61, 53]
# Merge = Array1 + Array2
# print(Merge)


# 24 WAP to find highest frequency element in array - Done
# A = []
# Size = int(input("Enter the size of A:"))
# for i in range(Size):
#     Value = int(input("Enter the value of A:"))
#     A.append(Value)
# Key = int(input("Enter the number which frequency needs to check:"))
# count = 0
# print("The original list is:", A)
# for i in range(Size):
#     if A[i] == Key:
#         count += 1
# print("The Number is:", Key ,"and the frequency is:", count)


# 25 WAP to add two number using recursion
# 26 WAP to find sum of digit of number using recursion.
