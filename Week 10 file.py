'''Assignment 10.1
This week we will create a program that performs file processing activities.  
Your program this week will use the OS library in order to validate that a 
directory exists before creating a file in that directory.  Your program will 
prompt the user for the directory they would like to save the file in as well 
as the name of the file.  The program should then prompt the user for their 
name, address, and phone number.  Your program will write this data to a comma 
separated line in a file and store the file in the directory specified by the user. 

Once the data has been written your program should read the file you just wrote 
to the file system and display the file contents to the user for validation purposes. 

Submit a link to your Github repository.'''


# Import OS library
import os


#file_name = input("Enter a file name: ")
file_name = 'contactinfo'
name = input("Enter your name: ")
address = input("Enter your address: ")
phone = input("Enter your phone number: ")


file_path = 'D:/Users/raych/Desktop/EDUCATION/Bellevue University/CIS 245 Intro to Programming/Week 10'
full_file = file_path + file_name


if os.path.isdir(file_path):
    print("The directory exists")
    
if os.path.isfile(file_name):
    print("The file path exists")

if os.path.exists(full_file):
    print("The file exists")

info = open(full_file, 'w+')
info.write(name + "," + address + "," + phone)
print(info.read())

