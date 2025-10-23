#Part one: For each line of code below, write what type of variable is being stored (string, integer, or float). Write your answer as a comment next to each line of code.

first_name = "Bro" # for example: this is a string
food = "pizza" #string
email = "Bro123@fake.com" #string
age = 25 #integer
quantity = 3 #integer
price = 10.99 #float
gpa = 3.2 #float
distance = 5.5 #float

#Part 2 – Predict the Output

#Without running the code, predict what each line will print:
print(f"Hello {first_name}") # for example: Hello Bro
print(f"You like {food}") # for example: You like pizza
print(f"Your email is: {email}") # your email is : Bro123@fake.com
print(f"You are {age} years old") # You are 25 years old
print(f"You are buying {quantity} items") #You are buying 3 items
print(f"The price is ${price}") # The price is $10.99
print(f"Your GPA is {gpa}") # Your GPA is 3.2
print(f"You ran {distance} km") #You ran 5.5 km


# Part 3 – Fix the Errors

# The following code has two mistakes.
# Find and fix them so it runs correctly.

name = "Bro"
food = "pizza"
print(f"Hello {name}")
print(f"You like {food}") #it forgot the ""

# Missing quotes and wrong variable name
food = "pizza"
print(f"You like {food}")

# Wrong f-string format
age = 17
print(f"You are {age} years old")

# Mismatched parentheses
price = 12.99
print(f"The total price is ${price}")
      

# Variable name spelled incorrectly
name = Bro
print(f"Hello {name}")

# Using + instead of commas
name = Bro
print(f"Hello " + {name})

# Mixing single and double quotes incorrectly
email = "Bro123@fake.com'
print(f"Your email is: {email}")

# Forgot to include the f before the string
age = 21
print(f"You are {age} years old")

# Trying to use a number as a variable
cool = "yes"
print(f"Am I cool? {cool}")
#rules: variable names cannot start with a number
#another rule is no spaces in variables names
#example my variable = 5 #incorrect
#correct my_variable = 5
#correct myVariable =5
#another rule is no special characters except
#example: my-variable =5 #incorrect
#correct: my_variable 5
#incorrect: my$variable =5 #incorrect
#correct:My_variable = 5
#no reserved keywords like class, def, return, etc.


# Missing curly braces
quantity = 3
print(f"You are buying {quantity} items")

# Using a reserved keyword
class1 = "ECS"
print(f"You are in {class1}")



# Part 4 – Create Your Own

# Write a short Python program that:

# Creates at least three variables (a string, an integer, and a float)

# Prints a formatted message using f-strings that combines all three.
#  Example:
movie = "Inception"
rating = 9.5
year = 2010
print(f"My favorite movie is {movie}, released in {year}, rated {rating}/10!")

artist = " Coldplay"
song= "yellow"
rating= 10

print(f"my favorite music artist is {artist}, My favorite song from him is {song}. I give him a rating of 10/{rating}")