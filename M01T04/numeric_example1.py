# PLEASE ENSURE YOU OPEN THIS FILE IN VS CODE OR A SIMILAR EDITOR otherwise you will not be able to read it.

# *** NOTE ON COMMENTS ***
# This is a comment in python. 
# Comments can be placed anywhere in Python code and the computer ignores them -- they are intended to be read by humans. 
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others. 


# ========= Declaring Numbers ========= 
# When you declare a variable Python will already know if it is a float or integer based on its characteristics.


# ************ Example 1 ************
print("Example 1: ")
ex1_number1 = 45 # 45 contains no fractional part so it is stored as an INTEGER
print(ex1_number1)
ex1_number2 = 12.52 # 12.52 contains the fractional part .52 so it is stored as a FLOAT
print(ex1_number2)


# ========= Casting Between Numeric Types ========= 
# To cast between numbers you make use of the int() or float() functions, depending on which is needed.


# ************ Example 2 ************
print("Example 2: ")
ex2_number1 = 12
ex2_number2 = 99.99
print(float(ex2_number1)) # The float() function casts the integer 12 to a float
print(int(ex2_number2)) # The int() function casts the float 99.99 to an integer. Note the output.

# Run this program to see the output 


# ========= Arithmetic Operations  ========= 


# ************ Example 3 ************
# Addition

print("Example 3: ")
sum_of_num = 2 + 4 # We can't use the keyword 'sum' as that is a built-in python function
print(sum_of_num)

cents = 0.25 + 4.33 
print(cents)


# ************ Example 4 ************
# Subtraction 

print("Example 4: ")
subtract = 3 - 7 
print(subtract) 

length = 34.90 - 23.23
print(length) 


# ************ Example 5 ************
# Multiplication 

print("Example 5: ")
multiply = 32 * 3.50
print(multiply)


# ************ Example 6 ************
# Division 

print("Example 6: ")
divide = 124 / 2.00
print(divide)


# ************ Example 7 ************
# Just like in maths, certain arithmetic operations take precedence over others
# What do you expect the following expressions to work out to?
# Write down what you think it will be, and then run the program to find out if you were correct

print("Example 7: ")
expression1 = 5 + 6 * 2
print("expression1 is: ", expression1)

expression2 = (5 + 6) * 2 
print("expression2 is: ", expression2)

expression3 = 6 * 4 - 10 / 5 * 2
print("expression3 is: ", expression3)

expression4 = ((15 + 5) - 10) / 2
print("expression4 is: ", expression4)

# ****************** END OF EXAMPLE CODE ********************* #
