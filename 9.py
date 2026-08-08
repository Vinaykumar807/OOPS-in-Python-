# File handling :- 
# It allows us to read from and write to files — a common task in almost every real-world application (storing data, logs, reports, etc.).

# Types :- 
# 'r' :- Read (default mode)	
# 'w' :-Write (overwrites if file exists)
# 'a' :-Append (adds content at the end)	
# 'x' :- Create (fails if file exists)	
# 'b' :- Binary mode	
# 't' :- Text mode (default)

# open file syntax

# file = open("file.name", "mode") 
# data = file.mode # like read , write , append 
# file.close()

# Read :-      # Which is used to read entire file 

file = open("demo.txt", "r")
data = file.read()
print(data)
file.close()

# Readline       # Which is used to read only sinlge line from the file 

file = open("demo.txt", "r")

line1  = file.readline()      # This will read the first line 
print(line1)

line2 = file.readline()        # This will raed the second line 
print(line2)

file.close()


# Readlines      # Which is used to read all lines from the file and store it in the "list"

file = open("demo.txt", "r")
data = file.readlines()
print(data)
file.close()


# Write    # Which is used to overwrite(Which means replace the new data to existing data) a file 

file2 = open("student.txt", "w") 
file2.write("Vinay\nShrusti\nVinnu\nChinnu")
file2.close()

# Append  # Which is used to add a new data at the end

file2 = open("student.txt", "a") 
file2.write("\nThis students are are my fav")
file2.close()

# r+ (read + write(overwrite)) = No Truncate = file will not delete like the data will be there 

file3 = open("college.txt","r+")
file3.write("123")                # This will overwrite to the existing data 
print(file3.read())             
file3.close()

# w+ (write(overwrite + read)) = Truncate = file wiped out (within teh file all data will be deleted )

file4 = open("family.txt", "w+")
file4.read()
file4.write("This is vinay ")
print(file4.read())
file4.close

# With :- Automatically closes the file (we don't need to write "close()" file)

with open("school.txt" , "w") as file5:
    file5.write("This is a school file")

with open("school.txt", "r") as file5:
    data = file5.read()
    print(data)

with open("school.txt" , "a") as file5:
    file5.write("\nthis file managed by manger")

with open("school.txt", "r") as file5:
    data = file5.read()
    print(data)

# Deleteing file 

with open("hi.txt","w") as file6:
    file6.write("Hi users ! ")

import os # OS = Opreating system 
os.remove("hi.txt")      # It will delete the existing file
