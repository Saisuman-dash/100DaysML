#printing grades based on marks 

marks = int(input("Enter total obtained marks !(0-100)"))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade : D")
else:
    print("Grade: F Better luck next time !")



#  Voter eligibility check based on citizenship
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen of India? (yes/no): ").strip().lower()
if age >= 18 and citizenship == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote ")


#Balance check menu for bank account 
print("Choose an option:")
print("1. Check balance")
print("2. Withdraw money")
print("3. Deposit money")
print("4. Exit")
option = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Your current balance is: ", 1000)
    case 2:
        print("withdrawl on process ")
    case 3:
        print("Deposit on process ")
    case 4:
        print("Exiting the program ")
    case _:
        print("Invalid choice ")

#Sum of odd numbers up to N

n = int(input("Enter a number: "))
sum_odd = 0

for i in range(1, n+1):
    if i % 2 == 0:
        continue
    sum_odd += i

print(f"Sum of all odd numbers from 1 to {n} is: {sum_odd}")

        