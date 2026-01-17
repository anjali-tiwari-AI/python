"""Mode 	Description
'r'	        Read mode (default). Opens the file for reading only.
'r+'        Read and write, text mode. The file pointer starts at the beginning.
'rb+'       Read and write, binary mode. The file pointer starts at the beginning.
'w'         Write-only, text mode (truncates existing file).
'wb'        Write-only, binary mode (truncates existing file).
'w+'        Write and read, text mode (truncates existing file).
'wb+'       Write and read, binary mode (truncates existing file).
'a'         Append-only, text mode. The file pointer is at the end of the file.
'ab'        Append-only, binary mode. The file pointer is at the end of the file.
'a+'        Append and read, text mode. The file pointer is at the end of the file.
'ab+'       Append and read, binary mode. The file pointer is at the end of the file.
'x'         Exclusive creation, text mode.
'xb'        Exclusive creation, binary mode.
'x+'        Exclusive creation, read and write, text mode.
'xb+'       Exclusive creation, read and write, binary mode
'b'	        Binary mode. Used with other modes (e.g., 'rb', 'wb') for non-text files like images or executables.
't'         Text mode (default). Data is read/written as strings.
'+'	        Update mode. Opens a file for both reading and writing (e.g., 'r+', 'w+', 'a+')"""

# Data = 

# In our daily life, we use many different types of characters to read, write, and communicate. 
# These characters include alphabets, numbers, and special symbols. 
# For example, when we write a simple sentence like Today is a good day, 
# we use lowercase letters such as a, b, c, d and sometimes uppercase letters like T or A. 
# Both uppercase letters such as A, B, C, D and lowercase letters such as a, b, c, d are important 
# because together they help us form meaningful words and sentences.


# Numbers are also a very important part of communication. We use 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9 to tell our age, 
# write phone numbers, calculate money, and mention dates like 2026 or time like 10:30. Without numbers, 
# it would be very difficult to manage daily activities such as shopping, studying, or traveling.


# Along with letters and numbers, special characters are widely used, especially in computers and mobile phones. 
# Symbols like @, #, $, %, &, *, !, ?, and _ are common in email addresses, passwords, usernames, and programming. 
# For example, an email address may look like this: user123@email.com
# , where letters, numbers, and symbols like @ and . work together. 
# Passwords often include characters such as A1@b#9 to make them strong and secure.


# We also use punctuation marks such as . , : ; ' " ( ) and - to make our sentences clear and meaningful.
# In mathematics and typing, symbols like +, -, =, <, >, /, and \ are used to show calculations or commands. 
# Even symbols like { } [ ] ~ and ` have special uses in computers and coding.


# So, whether we are writing ABC in school, typing abc on a keyboard, counting 123, or using symbols like !@#$ in technology, 
# all these characters together help us communicate properly. 
# They make our language complete and our digital world easy to use and understand.


#==============================Read to a file ================================================
#------------------------------------
# f = open("Basics\\Text.txt", "r")
# Data = f.read()
# print(Data)
# print(type(Data))
# f.close()
# print(len(Data))
# f.close()


#-------------------------------
# f = open("Basics\\Text.txt", "r")
# Line1 = f.readline()
# Line2 = f.readline()
# Line3 = f.readline()
# print(Line1)
# print(Line2)
# print(Line3)
# f.close()


#-------once we read the data then we need to close it if wants to read line by line again becuase courser will be in the last------------
# f= open("Basics\\Text.txt", "r")
# Data = f.read()
# print(Data)

# Line1 = f.readline()
# Line2 = f.readline()
# print(Line1 , "Hello")
# print(Line2, "Byebye")
# f.close()



#========================= Writing to a file ====================================================
# W = over write (errase then write)
# a = append write (Add at the end) 


# f= open("Basics\\Text.txt", "w")
# f.write("Hello, This is Anjali and i am a AI Developer or Engineer")
# f.close()



# f= open("Basics\\Text.txt", "a")
# f.write(" and i have developed an AI which is creating thousand of the job a day.\ni have established my own company. \nIt is a global company")
# f.close()

#============ Create a file and delete a file ========================================
# Create = open("Sample File.txt", "w")
# Create.close()

# C = open('Append file.txt', "a")
# C.close()

# Create.delete()


#====================== R+ (Over write a file i.e. delete a data )=================
# f= open("Basics\\Text.txt", "r+")         # R+ = Over write
# f.write("I am learning python")
# print(f.read())
# f.close()


#=================== W+ (it truncate the whole file first then we cn write) =========================
# F = open("Basics\\Text.txt", "w+") 
# print(F.read())  # Will get empty file then we need to write
# Write = F.write("I have complated python and now i am expert in AI")
# F.close()


# #============== a+ (It will not over write or errase rather it will be append in the last ) ==========================================
# F = open("Basics\\Text.txt", "a+")
# print(F.read())
# F.write(" Now, i started to work on library and AI/ML.")
# F.close()


#====================== With (open) Syntax =============================================




#======================= PROJECT =========================================
# Count = 0
# Open = open("Basics\\Text.txt", "r+")
# print(Open)
# Open.close()

F = open("Basics\\Text.txt", "w+") 

print(F.read())  # Will get empty file then we need to write
Write = F.write("I have complated python and now i am expert in AI")
print(Write)
F.close()