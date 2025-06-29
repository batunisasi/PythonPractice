#user input is a way to get data from the user during program execution
name = input("Enter your name: ")
age = int(input("Enter your age: ")) #the input function returns a string, so we convert it to an integer using int()
favorite_food = input("Enter your favorite food: ")

print(f"Hello, {name}! You are {age} years old and your favorite food is {favorite_food}.")

# You can also use input() to get multiple values at once
x, y = input("Enter two numbers separated by a space: ").split()
print(f"You entered: {x} and {y}")

# If you want to get a list of values, you can use a loop
numbers = [] # Initialize an empty list to store numbers
while True: 
    num = input("Enter a number (or 'done' to finish): ")
    if num.lower() == 'done':  # Check if the user wants to finish input #the lower() method converts the string to lowercase, so it will match 'done' regardless of case
        break # Exit the loop if 'done' is entered
    numbers.append(int(num))  # Convert input to int and add to the list
    #the append() method adds an item to the end of the list
print(f"You entered the numbers: {numbers}")

