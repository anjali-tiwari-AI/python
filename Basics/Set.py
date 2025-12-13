#Propertise = Unordered , No duplicate values, Mutable, Empty = set()


# Creting empty set
# S = set()
# print(type(S))


#--------------------------------------------------------------------------------------------------------
# Se = { 12, 45, 36, 85, 69}    #We can't use range founction here becuase their is no indexing in set 
# print(Se)
# for i in Se:
#     print(i)
    
    
    
#------------------------Methods---------------------------
# S = set()
# print(S)
# S.add(52)
# print(S)

#-------------Multiple values need to add at the 1 times only--------------------
# Set = set()
# print(Set)
# N = int(input("How many values:-"))
# for i in range(1, N+1):
#     Value = int(input('Enter the values here:- '))
#     Set.add(Value)
# print(Set)

# Set.update({25, 63, 85})   #added multiple values 
# print(Set)


#-----------Built-in methods --------------------------------
# ['add', 'clear', 'copy', 'difference', # '# difference_update', # 'discard', 
# 'intersection', 'intersection_update', 'isdisjoint', 'issubset', # 'issuperset', 
# 'pop', # 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# print(dir(set))

#-------------------------ADD------------------
# S = set()
# Numbers = int(input("Enter the number of times of the value:- "))
# for i in range(1, Numbers+1):
#     Values = int(input("Enter the values:- "))
#     S.add(Values)

# print(S)
# Sum = 0
# for j in S:
#     Sum = Sum + j
# print(Sum)
# print(type(S))
    
#-----------Clear----------------
# S = set()
# Numbers = int(input("Enter the number of times of the value:- "))
# for i in range(1, Numbers+1):
#     Values = int(input("Enter the values:- "))
#     S.add(Values)

# print(S)
# print(type(S))
# S.clear()
# print(S)


#------Copy---------------
# S = set()
# Numbers = int(input("Enter the number of times of the value:- "))
# for i in range(1, Numbers+1):
#     Values = int(input("Enter the values:- "))
#     S.add(Values)

# print("Without copy", S)
# Copy = S.copy()
# print("After copy", Copy)
# Copy.add('Copy')

# S.clear()
# print("After copy and adding elements", Copy)
# print("After clear", S)


#-----------difference------------------

"""In Python, the difference_update() method for sets modifies the original set by removing any elements that are also 
present in one or more other specified sets (or iterables).

Here's a breakdown of its meaning and behavior:
In-place modification: Unlike the difference() method, which returns a new set containing the difference, 
difference_update() directly alters the set on which it's called. It does not create a new set.

Removing common elements: It identifies elements that exist in both the calling set and the set(s) provided as arguments.
These common elements are then removed from the calling set.
Return value: The difference_update() method returns None, as its primary purpose is to modify the set in place, 
not to produce a new value."""


# S1 = set()
# Numbers1 = int(input("Enter the number of times of the value:- "))
# for i in range(1, Numbers1+1):
#     Values1 = int(input("Enter the values:- "))
#     S1.add(Values1)
    
# S2 = set()
# Number2 = int(input("Enter the number of times of the values:- "))
# for i in range(1, Number2+1):
#     Values2= int(input("Enter the values:- "))
#     S2.add(Values2)

# Difference = S1.difference(S2)   #The element which is not in set2 but have in set1 we will accordingly the value
# print(Difference)


# Note: Difference C = {a} - {b} and Differnce_update = A = A - B
#--------------difference_update------------------------------it is updating the set which is given first time  
# Set1 = {"Nishant", "Piyush", 'Shubham'}
# Set2 = {"Ram", "Shyam", "Nishant", "Aman"}
# print("Before Differnce_update method Set1", Set1)
# Set1.difference_update(Set2)
# print("After difference_update method Set1", Set1)
# print("Their is no change in set2 after difference_update method Set2", Set2)


#---------------discard----------------Remove built-in through error if element is not in set but discard element doesn't works
# S = set()
# Number = int(input("Enter the number of times of the values:- "))

# for i in range(0, Number):
#     Values = input("Enter the values:- ")
#     S.add(Values)
    
# print("Normal Set values", S)
# S.discard("Apple")
# print(S)



#-------------intersection--------------------------------------Gives common values
# S1 = set()
# Numbers1 = int(input("Enter the number of times of the value:- "))
# for i in range(1, Numbers1+1):
#     Values1 = input("Enter the values:- ")
#     S1.add(Values1)
    
# S2 = set()
# Number2 = int(input("Enter the number of times of the values:- "))
# for i in range(1, Number2+1):
#     Values2= input("Enter the values:- ")
#     S2.add(Values2)

# Common_value_intersection = S1.intersection(S2)
# print(Common_value_intersection)


#----------------intersection_update------------------Gives values in the first entered set and it will be common in all set 
# S1 = set()
# Numbers1 = int(input("Enter the number of times of the value:- "))
# for i in range(1, Numbers1+1):
#     Values1 = input("Enter the values:- ")
#     S1.add(Values1)
    
# S2 = set()
# Number2 = int(input("Enter the number of times of the values:- "))
# for i in range(1, Number2+1):
#     Values2= input("Enter the values:- ")
#     S2.add(Values2)


# Common_value_intersection = S1.intersection_update(S2)
# print(Common_value_intersection)
# print(S1)
# print(S2)


#----isdisjoint-------if their is a relationship in 2 sets then it is not disjoint and if their is no relationship then it is disjoint
# if no common elements in both sets is called isdisjoint

# Set1 = set()
# Set1_no = int(input('Enter the number of times for set1:- '))
# for i in range(1, Set1_no+1):
#     Value = input('Enter the values:- ')
#     Set1.add(Value)


# Set2 = set()
# Set2_no = int(input('Enter the number of times for set1:- '))
# for i in range(1, Set2_no+1):
#     Value = input('Enter the values:- ')
#     Set2.add(Value)


# print("Set1 values:", Set1)
# print("Set2 values:", Set2)
# print("Give the common values in intersection:-", Set1.intersection(Set2))
# print("Do we have common elements or it is disjoint(No common value):-", Set1.isdisjoint(Set2))


#-----------issubset--------When a set's all emements are present in another set then it is subset else not and output (true or false)
# Nums1 = set(range(1, 101))
# Nums2 = {12, 45, 36, 84, 26, 75}
# Is_Sub_set = Nums2.issubset(Nums1)
# print(Is_Sub_set)     #True output

# Is_Sub_set = Nums1.issubset(Nums2)
# print(Is_Sub_set)               #False Output


#-----------Issuperset---------True if all items in the specified set exists in the original set, otherwise it return false
# A = {1, 2, 3, 4, 5, 6}
# B = {1, 2, 3}
# print(A.issuperset(B))



#----Pop-----It removes the first element from the output but the their is no order of the output that's why the element can be anything
# Set1 = set()
# Set2 = set()
 
# Numbers_set1 = int(input("Enter the number of times of the values in set1: "))
# Numbers_set2 = int(input("Enter the number of times of values in set2: "))

# for i in range (1, Numbers_set1+1):
#     Values_Set1 = input("Enter the set1 values: ")
#     Set1.add(Values_Set1)

# for j in range(1, Numbers_set2+1):
#     Values_Set2 = input("Enter the set2 values: ")
#     Set2.add(Values_Set2)
    

# print("Before pop method set1 is ", Set1)
# print("Before pop method set2 is ", Set2)
# print("The element which is going to removed from pop method is in set1:", Set1.pop())
# print("After pop method the output of the set1 is ", Set1)
# print("The element which is going to removed from pop method is in set2:", Set2.pop())
# print("After pop method the output of the set2 is ", Set2)


#----------Remove-------------it removes a particular element from the set
# Remove1 = set()
# Remove2 = set()

# Values_Remove1 = int(input('Enter the number of times you wants to enter the values in Remove1 set: '))
# Values_Remove2 = int(input('Enter the number of times you wants to enter the values in remove2 set: '))

# for i in range(1, Values_Remove1 +1):
#     Remove1_values = input("Enter the remove1 set's values: ")
#     Remove1.add(Remove1_values)
    

# for j in range(1, Values_Remove2+1):
#     Remove2_values = input("Enter the remove2 set's values: ")
#     Remove2.add(Remove2_values)

# print("Original values of remove1 set is: ", Remove1)
# print("original values of remove2 set is: ", Remove2)

# print("After remove method the values of set1 is:", Remove1.remove(input("Enter the values which you wants to remove from Remove1 set:")))
# print("After remove method the values of set2 is:", Remove2.remove(input('Enetr the values which you wants to remove from Remove2 set:')))

# print("After remove built-in method the new set of the remove1 is:", Remove1)
# print("After remove built-in method the new set of the remove2 is:", Remove2)


#----------symmetric_difference---------------------------------it returns uncommon elements of both the sets
# S1 = {10, 20.5, "Python", (10, 20)}
# S2 = {20, 3.5, "Python 3", (10, 20), (50, 10)}

# Res = S1.symmetric_difference(S2)
# print(Res)


#----------Symmetric_difference_update---------It modifies an existing set to contain only the elements that 
# are present in either the original set or a second specified set, but not in both (their intersection)
# Symmetric_difference1 = set()
# Symmetric_difference2 = set()


# # S1 = {10, 20.5, "Python", (10, 20), ("India", "China", "USA"), "Hello India"}
# # S2 = {20, 3.5, "Python 3", (10, 20), (50, 10), ("India, "China", "USA")}


# S1 = Symmetric_difference1 
# S2 = Symmetric_difference2

# Symmetric_difference1_Count = int(input('Enter the number of times you wants to enter the values in Symmetric_difference1 : '))
# Symmetric_difference2_Count = int(input('Enter the number of times you wants to enter the values in Symmetric_difference1 : '))

# for i in range(1, Symmetric_difference1_Count+1):
#     Values1 = input("Enter the values for first Symmetric_difference1: ")
#     Symmetric_difference1.add(Values1)
    
# for j in range(1, Symmetric_difference2_Count+1):
#     Values2 = input("Enter the values for first Symmetric_difference2: ")
#     Symmetric_difference2.add(Values2)

# print("Before Symmetric_difference_update method: ", S1)
# print("Before Symmetric_difference_update method: ", S2)

# S1.symmetric_difference_update(S2)
# print("After Symmetric_difference_update method: ", S1)


#---------------Union--------------------------set containing all the unique elements from both original sets or 
# combine all elements from both sets and remove any duplicates

# Union1 = {"Hello India", (100, 500), ("India", "China", "Japan")}
# Union2 = {"Anjali_AI", (100, 500), ("India", "China", "Japan"), "Data Science", 500 , "Anjali is the best"}


# Union_Result = Union1.union(Union2)
# print("All single values from both sets and duplicate value will be only 1 time in the output:", Union_Result)


# ----------------Update---------------------------
# S1 = {1, 2, 3}

# print("Original values:", S1)

# S1.add("Anjali is the best")

# print("After adding the values:", S1)

# S2 = {100, 200, 300}

# S1.update(S2)
# print("After using update built-in method", S1)


#========================= COMPLETED ALL BUILT-IN METHODS ====================================================================================================================
#==========================================================================================================================================

