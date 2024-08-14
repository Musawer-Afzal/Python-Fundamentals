print('Hello World, I am learning Python')
print('Hello', 23 + 4, 'World', sep='|')
print(3, 5)

# Data Types
# Integer
print(4)

# Float
print(3.14)

# String
print('Hello World')

# Boolean
print(True)
print(False)

# List(Array)
print([1, 2, 3, 4, 5])

# Tuple
print((1, 2, 3, 4, 5))

# Dictionary
print({'name': 'John', 'age': 30 , 'Wight' : 55})

# Set
print({1, 2, 3, 4, 5})

# complex
print(3 + 4j)

# None
print(None)

# Types
print(type(4))
print(type(3.14))
print(type('Hello World'))
print(type(True))
print(type([1, 2, 3, 4, 5]))
print(type((1, 2, 3, 4, 5)))
print(type({'name': 'John', 'age': 30, 'weight': 55}))
print(type({1, 2, 3, 4, 5}))
print(type(None))


# Dynamic Binding
x = 5
print(x)
x = 'Hello World'
print(x)

# Static Binding
# int x = 5
# string y = 'Hello World'
# print(x)
# print(y)

# Syntax
a,b,c = 1,2,3
print(a,b,c)

a = b = c = 5
print(a,b,c)

# Identifiers Rules
# You can never start with a number.
# You can use letters, numbers, and underscores.
# You can't use any special characters except underscore " _ ".
# You cannot use keywords as identifiers.


# Add Numbers taken from user
# Take Input from User
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
# Add the Numbers
#result = num1 + num2
# Print the result
#print(result)



# DataType Conversion(Explicit Conversion)
type(str(4))
type(int(4.0))
type(float(4))



# Literals
a = 0b1010 # Binary Literal
print(a)
b = 100 # Decimal Literal
print(b)
c = 0o310 # Octal Literal
print(c)
d = 0x12c # Hexadecimal Literal
print(d)

# Float Literal
float_1 = 10.5
print(float_1)
float_2 = 1.5e2
print(float_2)

# Complex Literal
x = 3.14j
print(x.real, x.imag)



# Strings
string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)  