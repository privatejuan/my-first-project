print("Hello, World!")
print("I am learning Python!")

name = "Paul"
age = 27
fortnightly_income= 1600

# Variables: Data stored in memory.

print("Name:", name)
print("Age:", age)
print("Fortnightly Income:", fortnightly_income)

rent = 500
remaining = fortnightly_income - rent

print("Rent Costs:", rent)
print("Remaining money:", remaining)

food = 100
spending = remaining - food 

print(f"Food Budget: {food}")
print(f"Remaining Money: {spending}")

# Calcualte saving percentage

savings = (spending / fortnightly_income) * 100

print(f"Savings Percentage: {savings:.2f}%")


# Inputs

name = input("What is your name? ")
age = int(input("What is your age? "))

print(f"\nHello {name}")
print(f"You are {age} years old.")

confirm = input("Is this correct? (yes/no): ")

if confirm.lower() == "yes":
    print(f"\nOverview: Name: {name}, Age: {age}")

else:
    print("Please restart the program and enter correct details.")