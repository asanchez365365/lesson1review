"""
Mini Calculator Challenge — f-strings + input + math
"""
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nResults:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
if b != 0:
    print(f"{a} / {b} = {a / b:.2f}")
    print(f"Remainder {a} % {b} = {a % b:.2f}")
else:
    print("Division and remainder by zero are undefined.")
print(f"Average = {(a + b) / 2:.2f}")
print(f"{a} squared = {a ** 2:.2f}")
print(f"{b} squared = {b ** 2:.2f}")
