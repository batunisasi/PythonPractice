#string variables
first_name = "steve"
food = "mie ayam"
email = "batunisasi@gmail.com"
game_name = "Red Dead Redemption 2"

print(f"Hello, {first_name}")
print(f"My favorite food is {food}")
print(f"My email is {email}")
print(type(email))

#integer variables
age = 18
height = 176
weight = 70 
print(f"i am {age} years old")
print(f"My height is {height} cm")
print(f"i am {weight} kilograms")
print(type(age))

#float variables, and some string variables
price = 10.99
rating = 4.5
print(f"i bought {game_name} for ${price}")
print(f"My rating for {game_name} is {rating} out of 5")
gpa = 4.27
print(f"My GPA is {gpa} out of 5.00")
print(type(price))

#boolean variables
is_student = True
gay = False

if is_student:
    print("I am a student") 
else:
    print("I am not a student")

if gay:
    print("i am gay")
else:
    print("i am straight")

print("i am gay" if gay else "i am straight")
print(type(gay))

#multiple values variable
#ex 1
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")
#ex 2
a = b = c = 69
print(f"x = {a}, y = {b}, z = {c}")
#ex 3
numbers = [1, 2, 3, 4, 5]
q, r, s, t, u = numbers
print (f"q = {q}, r = {r}, s = {s}, t = {t}, u = {u}")

#global variables
L = 10
def calculate_area():
    area = L * L
    print(f"The area of the square is {area}")
    
calculate_area()    