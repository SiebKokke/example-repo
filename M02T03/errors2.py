# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #syntax error, missing quotes to make it a string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" #logical error, siwtch the animal_type and number_of_teeth, also need to add the f in front of the string to make it formatted 

print(full_spec) #sytnax error, missing parentheses

