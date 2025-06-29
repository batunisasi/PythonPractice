#Python Data Types, By Batunisasi

#text type = str
#numeric types = int, float, complex
#sequence types = list, tuple, range
#mapping type = dict
#set types = set, frozenset
#boolean type = bool
#binary types = bytes, bytearray, memoryview
#none type = NoneType

#EXAMPLE 1: String type
first_name = "Batunisasi" #str

#EXAMPLE 2: Numeric type
age = 30 #int
pi = 3.14 #float
complex_number = 2 + 3j #complex

#EXAMPLE 3: Sequence types
fruits = ["apple", "banana", "cherry"]  # List
vegetables = ("carrot", "broccoli", "spinach")  # Tuple
numbers_range = range(1, 10)  # Range
#the difference between list and tuple is that list is mutable (can be changed) while tuple is immutable (cannot be changed)
#range is a sequence of numbers, which can be used in for loops or to create lists

#EXAMPLE 4: Mapping type
person = dict(name="Batunisasi", age=18, University="Universitas Diponegoro", hobbies=["gaming", "playing music", "coding"]) # Dictionary
print(person) 
#dictionaries are used to store data values in key:value pairs, where each key is unique and maps to a value

#EXAMPLE 5: Set types
fruits_set = {"apple", "banana", "cherry"}  # Set
fruits_frozenset = frozenset(["apple", "banana", "cherry"])  # Frozenset
#the difference between set and frozenset is that set is mutable/unordered (can be changed) while frozenset is immutable/ordered (cannot be changed)

#EXAMPLE 6: Boolean type
is_student = True  # bool
is_employed = False  # bool

#EXAMPLE 7: Binary types
binary_data = bytes([65, 66, 67])  # Bytes
byte_array_data = bytearray([65, 66, 67])  # Bytearray
memoryview_data = memoryview(bytes([65, 66, 67]))  # Memoryview
print(memoryview_data)
#bytes are immutable sequences of bytes, bytearray is a mutable sequence of bytes, and memoryview is a view of the bytes object that allows you to access the data without copying it

#EXAMPLE 8: None type
none_value = None  # NoneType
#None is a special constant in Python that represents the absence of a value or a null value
#You can use None to indicate that a variable has no value or to represent the absence of a value in a function return
print(none_value)

#TYPECASTING
#Typecasting is the process of converting a variable from one data type to another
age = float(age)  # Convert int to float
print(age)  # Output: 30.0
pi = int(pi)  # Convert float to int
print(pi)  # Output: 3
complex_number = complex(age)  # Convert int to complex
print(complex_number) # Output: (30+0j)
#Convert string to int
number = "42"
number = int(number)
print(number)  # Output: 42
#Convert string to boolean
username1 = "Batunisasi"
username1 = bool(username1) 
print(username1) #output: True
username2 = ""
username2 = bool(username2)
print(username2) #output: False
#The typecasting from string data type to boolean data type will be useful for a user login interface
