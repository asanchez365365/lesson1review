# Goal: show how input works, type conversion, and basic math output.


print("Welcome! We'll do some math.\n")
#input is how you get user data 
name= input ("what's your name?")
print(f"Hello,{name}!\n")
#get two numbers from the user
num1= int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(f"You entered {num1} and {num2}.")
print(num1 + num2, " is what you get if you just add them as a text")


# Get two numbers from the user and ask for their name to personalize the experience















# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings