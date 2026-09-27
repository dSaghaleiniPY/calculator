import math
# used ai for float(makes the numbers into usable numbers, not text)
a = float(input("x = ... "))
b = float(input("y = ... "))
operation = input("*, -, +, or /? ")
if operation == "+":
    print(int(a + b))
if operation == "-":
    print(int(a - b))
if operation == "*":
    print(int(a * b))
if operation == "/":
    print(int(a/b))