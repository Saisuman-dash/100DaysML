
#variables and data types and basic DSA qs

name = "suman"
age = 21
height = 5.7
is_student = True

print(type(height))

age_str = str(age)

#take n numbers as input and print their sum 

nu=input(("Enter number of terms to add \n"))
n = int(nu)
sum = 0
for i in range (n):
    num = input(f"Enter the {i+1} number")
    sum += int(num)

print(f"Sum total is {sum}")

#ask a number and print it as even or odd 

num = input("Enter a number to check it is even or odd ? \n").strip()
n = int( num )

if n % 2 == 0 :
    print(f"Number {n} is a even number . \n")
else : 
    print(f"The number {n} is a odd number . \n")  #print the number as well

#we can use type () function to check the data type of a variable in python 


