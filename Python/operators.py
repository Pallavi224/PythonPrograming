# Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)       # Output: 13
print("Subtraction:", a - b)    # Output: 7
print("Multiplication:", a * b) # Output: 30
print("Division:", a / b)       # Output: 3.333...
print("Modulus:", a % b)        # Output: 1
print("Exponentiation:", a ** b) # Output: 1000
print("Floor Division:", a // b) # Output: 3

# Comparison Operators
print("Equal:", a == b)         # Output: False
print("Not Equal:", a != b)     # Output: True
print("Greater Than:", a > b)   # Output: True
print("Less Than:", a < b)      # Output: False
print("Greater or Equal:", a >= b) # Output: True
print("Less or Equal:", a <= b) # Output: False

# Logical Operators
x = True
y = False
print("Logical AND:", x and y)  # Output: False
print("Logical OR:", x or y)    # Output: True
print("Logical NOT:", not x)    # Output: False

# Bitwise Operators
c = 5  # Binary: 0101
d = 3  # Binary: 0011
print("Bitwise AND:", c & d)    # Output: 1 (Binary: 0001)
print("Bitwise OR:", c | d)     # Output: 7 (Binary: 0111)
print("Bitwise XOR:", c ^ d)    # Output: 6 (Binary: 0110)
print("Bitwise NOT:", ~c)       # Output: -6 (Inverts all bits)
print("Left Shift:", c << 1)    # Output: 10 (Binary: 1010)
print("Right Shift:", c >> 1)   # Output: 2 (Binary: 0010)

# Assignment Operators
e = 10
e += 5  # Equivalent to e = e + 5
print("After +=:", e)           # Output: 15
e *= 2  # Equivalent to e = e * 2
print("After *=:", e)           # Output: 30

# Membership Operators
lst = [1, 2, 3, 4, 5]
print("Is 3 in list?", 3 in lst)    # Output: True
print("Is 6 not in list?", 6 not in lst) # Output: True

# Identity Operators
f = [1, 2, 3]
g = [1, 2, 3]
print("f is g:", f is g)           # Output: False (Different objects)
print("f is not g:", f is not g)   # Output: True