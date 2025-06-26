#importing system module for error code exiting
import sys

#--------------------------
# Input & Validation Block
#--------------------------

# Taking user input of name and age and handling extra spaces and formatting it to the name sttyle accordingly
name = input("What is your name? :").strip().title()

#taking age input as string and removing any spaces / strip removes extra spaces
age = input("How old are you? :").strip()

#Checking if age is a number or not 
if not age.isdigit():
    print("Invalid input ❌. enter the age in integer only .")
    sys.exit() #exits from the code

#if entered digit it will be stored as string so typecast
agei=int(age)

#printing age and name using f string
print(f"Name : {name} , Age : {agei}")

#check age eligibility for voting
if agei >=18:
    print(f"{name} Verified! You are eligible for voting")
else:
    print(f"{name} you are not eligible for voting .")

#for loop printing even numbers till age 
print("These are the even numbers till your entered age.")
for i in range (2 , agei+1 , 2): #using start,stop,step 
    print(i,end=" ") #end is used to print numbers in one line 

#while loop 
print("\nThese are the even numbers till your entered age using while loop")
n=0
while n<= agei:
    print(n , end=" ")
    n += 1


# Function that takes user name and returns a greeting
def greet(user):
    return f"🎉 Hello, {user}! Glad to have you here."

# Calling the function and printing returned greeting
print("\n" + greet(name))

