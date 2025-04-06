# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #syntax error, missing parentheses
print ("\n") #syntax error, missing parentheses and uneeded indentation

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #syntax errror,indentation not needed, age_Str is not declared because they used == instead of =, alo need to convert to integer
age = int(age_Str) #syntax error, age_Str is a string and needs to be converted to an integer 
print("I'm", age, "years old.") #syntax error switch the + to commas since we cant concatinate a string and an integer

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 #syntax error, indentation is not needed, need to convert to integer 
total_years = age + years_from_now

print("The total number of years:", total_years) #syntax error, print statement is not correct, answer_years is not declared and needs to switched to total_years, switch + to commas    

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = (int(total_years) * 12) + 6 #syntax error, total_years is a string and needs to be converted to an integer also a logical error, need to add 6 months to the total 
print("In 3 years and 6 months, I'll be ", total_months, "months old") #syntax error, print statement is not correct, total_months is a string and needs to be converted to an integer, switch + to commas

#HINT, 330 months is the correct answer

