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


#---------------discard-------------------------Remove built-in through error if element is not in set but discard element doesn't 
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


#---------------isdisjoint---------------------





# ', '', '', 'issubset', # 'issuperset', 
# 'pop', # 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update