# #                                         # Methods to define Dictionary
# # # Method 1: ==========================================================

# # student = {
# #     "Name":"Anjali",
# #     "Course":"Python",
# #     "Time":330,
# #     "FeesPerYear":20000,
# #     "Total_Duration":1.5
# #     }

# # # Method 2: ==========================================================
# # student2 = dict(name="Rajat",course="Java",time=430)


# #                                         # Method to access dictionary elements
# #
# # # Method 1: ==========================================================
# # # value= dict_name["keyName"]

# # fees=student["FeesPerYear"]
# # duration=student["Total_Duration"]
# # total_fees=fees+duration

# # # Method 2: ==========================================================
# # # value= dict_name.get("keyName")

# # fees=student.get("FeesPerYear")
# # duration=student.get("Total_Duration")
# # total_fees=fees+duration


# # print("Student dictionary",student) #Accessing whole dictionary


# # print(student2["name"]) #Accessing single data Way 1
# # print(student.get("grade")) #Provides None if no Key present
# # print(student.get("grade","Sahi value daal")) #Accessing single data Way



# # student = {
# #     "Name":"Anjali",
# #     "Course":"Python",
# #     "Time":330,
# #     "FeesPerYear":20000,
# #     "Total_Duration":1.5
# #     }

# # # print("Old Dictionary",student)

# # #student["FeesPerYear"]= 100000          # Updating data in already existing key
# # student["course2"] = "Data Science"     # Adding a new key and data

# # student.update({"Course":"NodeJs","Time":430,"FeesPerYear":30000}) # Updating Multipls data in already existing key

# # del student["course2"]

# # # student.popitem()
# # # student.clear()

# # # print("New Dictionary",student)

# # for key in student:
# #     print(key,":",student[key])

# # for key,value in student.items():
# #     print(key,":",value)

# # # ==================================================Accessing list==================================================

# # # print(student.keys())
# # # print(student.values())
# # # print(student.items())



# # # student = 
# # # {
# # #     "Name":"Anjali",
# # #     "Course":"Python",
# # #     "Time":330,
# # #     "FeesPerYear":20000,
# # #     "Total_Duration":1.5
# # #     }

# # # [1,2,3]

# # students = {
# #     101:{
# #     "Name":"Anjali",
# #     "Course":"Python",
# #     "Time":330,
# #     "FeesPerYear":20000,
# #     "Total_Duration":1.5
# #     },
# #     102:{
# #     "Name":"Rahul",
# #     "Course":"Java",
# #     "Time":430,
# #     "FeesPerYear":200,
# #     "Total_Duration":2,
# #     "Subject":{
# #         "Math":200,
# #         "Physics":100,
# #         "Chem":50
# #     }
# #     }
# # }

# # print(students[102]["Subject"].items())
# # print(students[102]["Subject"].keys())
# # print(students[102]["Subject"].values())

# # print(students[101].keys())

# # print(students[102]["Subject"]["Math"])

# # students[rollNo][StudentDetailName][SubjectName]

# # if StudentDetailName is subject add another dimension


# #============================================================================================================================================================
# =========================================== Python Dictionary Practice Questions ========================================================================
# ====================================================================================================================================
# 1. Create a dictionary from a string such that keys are characters and values are how many times they appear,
# but exclude spaces.




# 2. Write a program to swap keys and values in a dictionary. What happens if two keys have the same value?
# 3. Write a program to find the key with the maximum length (string length) in a dictionary.
# 4. Write a program to check if all values in a dictionary are unique.
# 5. From a dictionary of fruits and prices, print only those fruits whose price is divisible by 5.
# 6. Create a dictionary where keys are numbers 1–20 and values are "even" or "odd" depending on the key.
# 7. Write a program to check whether a dictionary is symmetric (same when keys and values are swapped).
# 8. Create a dictionary from a string but only include vowels as keys with their counts.
# 9. Write a program to delete a key from a dictionary if its value is the smallest among all values.
# 10. Write a program to find the sum of values of all keys that start with the letter "a".
# 11. Create a dictionary where keys are numbers from 1–10 and values are "prime" or "not prime".
# 12. Write a program to filter out all dictionary items whose value is not an integer.
# 13. Write a program to replace all values in a dictionary with their string lengths (if they are strings).
# 14. Write a program to count how many dictionary values are lists.
# 15. Given a dictionary of words and meanings, reverse the dictionary so meanings become keys and words
# become values (if possible).
# 16. Write a program to extract all dictionary keys that are of type int.
# 17. Create a dictionary that maps each digit (0–9) to how many times it appears in a given number.
# 18. Write a program to multiply all numeric values in a dictionary.
# 19. Create a dictionary where keys are numbers 1–5 and values are dictionaries with keys "square" and "cube".
# 20. Write a program to check if two dictionaries are disjoint (no common keys).
# 21. Write a program to merge two dictionaries but keep the maximum value for each key if keys overlap.
# 22. Write a program to find the average of numeric values in a dictionary.
# 23. Write a program to count how many values in a dictionary are themselves dictionaries.
# 24. Write a program to extract the second largest value from a dictionary.
# 25. Write a program to find the key(s) whose values are repeated the most times.
# 26. Write a program to create a dictionary from a list of numbers where keys are numbers and values are the
# sum of their digits.
# 27. Write a program to group words by their length using a dictionary.
# 28. Given a sentence, create a dictionary where keys are words and values are how many vowels each word
# contains.
# 29. Write a program to group numbers in a list by whether they are divisible by 2, 3, or 5, using a dictionary.
# 30. Write a program to create a dictionary where keys are characters in a string and values are lists of their
# positions in the string.
# 31. Write a program to remove all dictionary keys that contain any digit in them.
# 32. Write a program to merge two dictionaries but store values as a list if keys overlap.
# 33. Write a program to group dictionary keys based on the data type of their values.
# 34. Write a program to create a dictionary of each alphabet letter mapping to the count of words starting with
# that letter in a sentence.
# 35. Write a program to check if a dictionary is a subset of another dictionary (both keys and values must match).
# 36. Write a program to "rotate" keys of a dictionary so that the first key becomes the last, and others shift
# forward.
# 37. Write a program to create a dictionary of squares but exclude numbers that end with digit 5.
# 38. Write a program to reverse a nested dictionary (keys and subkeys become inverted).
# 39. Write a program to create a dictionary from a list of tuples but keep only the last value if a key appears
# multiple times.
# 40. Write a program to find the difference between values of the largest and smallest keys in a dictionary
# (assuming numeric keys).
# 41. Write a program to check if a dictionary is "palindromic" — i.e., reading keys in order equals reading values
# in order.
# 42. Write a program to extract all paths from a nested dictionary (like flattening JSON into key paths).
# 43. Write a program to build a dictionary where keys are words and values are whether they are palindrome or
# not.
# 44. Write a program to create a dictionary that maps numbers 1–100 to "Fizz", "Buzz", "FizzBuzz", or the number
# itself (FizzBuzz dictionary).
# 45. Write a program to create a dictionary of numbers 1–20 where values are "prime factors" of the number
# (list).
# 46. Write a program to check if all values in a nested dictionary are greater than 10.
# 47. Write a program to flatten a nested dictionary where sub-keys get concatenated with parent keys using _.
# 48. Write a program to generate a dictionary from a matrix where each row number is the key and row values
# are the list.
# 49. Write a program to create a dictionary that counts how many times each digit appears across all values of
# another dictionary.
# 50. Write a program to create a dictionary where keys are words and values are the set of unique letters in that
# word.
