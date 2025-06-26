#Day 1 python basics
name = input("what is your Name? : ")
age = int(input("Enter your age: "))
print("Name and age of the user is : " + name ,age)


#conditional logic
if age>=18:
    print("Congrats ! You are eligible for voting ")
else:
    print("You are not eligible for voting !")


#looping example (for loop)
print("The numbers till your age are :")
for i in range(1,age):
    print(i)

# While Loop
print("Countdown from your age :")
x = 18
while x>0:
    print(x)
    x-=1

#Function Example
def greet(user): 
    return f"Hello ! {user} ! Good to see you here bhai"
print(greet(name))

#f string use 
dataname = "suman"
print(f"Hello {dataname} !")
