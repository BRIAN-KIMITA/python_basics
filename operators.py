#arithmetic operators
x=7
y=3
print(x+y) #addition
print(x-y) #subtraction
print(x/y) #quotient
print(x%y) #modulus
#comparison operators
a=12
b=34
print(f"varible {a} is equal to variable {b} {a==b}")
print(f"varible {a} is  not equal to variable {b} {a!=b}")
print(f"varible {a} is greater than variable {b} {a>b}")
print(f"varible {a} is  greater or equal to variable {b} {a>=b}")
print(f"varible {a} is  less than t variable {b} {a<b}")
print(f"varible {a} is  less or equal to variable {b} {a<=b}")
#logical operators
c=5
print(f"is this statement true no its {c>2 and c<5}")
# Arithmetic operators used between two operands for a particular operation.
# There are many arithmetic operators. It includes the exponent (**)
# operator as well as the + (addition), - (subtraction), * (multiplication),
# / (divide), % (reminder), and // (floor division) operators.
a = 32  # Initialize the value of a
b = 6  # Initialize the value of b
print('Addition of two numbers:', a + b)
print('Subtraction of two numbers:', a - b)
print('Multiplication of two numbers:', a * b)
print('Division of two numbers:', a / b)
print('Reminder of two numbers:', a % b)
print('Exponent of two numbers:', a ** b)
print('Floor division of two numbers:', a // b)

# Comparison operator
# Comparison operators mainly use for comparison purposes. Comparison operators compare the values of the two operands and return a true or false Boolean value in accordance. The example of comparison operators are ==, !=, <=, >=, >, <.
# In the table below, we explain the works of the operators.
a = 32      # Initialize the value of a
b = 6       # Initialize the value of b
print('Two numbers are equal or not:',a==b)
print('Two numbers are not equal or not:',a!=b)
print('a is less than or equal to b:',a<=b)
print('a is greater than or equal to b:',a>=b)
print('a is greater b:',a>b)
print('a is less than b:',a<b)
# Assignment Operators
# Using the assignment operators, the right expression('s value is assigned to the left operand. '
# 'There are some examples of assignment operators like =, +=, '
# -=, *=, %=, **=, //=. In the below table, we explain the works of the operators.)
a = 32  # Initialize the value of a
b = 6  # Initialize the value of b
print('a=b:', a == b)
print('a+=b:', a + b)
print('a-=b:', a - b)
print('a*=b:', a * b)
print('a%=b:', a % b)
print('a**=b:', a ** b)
print('a//=b:', a // b)
a = 5  # initialize the value of a
print('Is this statement true?:',a > 3 and a < 5)
print('Any one statement is true?:', a > 3 or a < 5)
print('Each statement is true then return False and vice-versa:', (not (a > 3 and a < 5)))