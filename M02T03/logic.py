#create a logical error 

age = "sieb"
name = "23"

if age == "sieb"
    print("You are sieb years old")
else:
    print("You are not sieb years old")

if name == "23":
    print("Your name is not 23, please get a new name")
else: 
    print("Your name is 23")

#althought the program runs without an error the output will make no sense. 
#age and name are mixed up. 
#the if else statements print out the wrong output and say you are "not" sieb years old when they should print out that you are.