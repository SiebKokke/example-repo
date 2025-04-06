#use a for function and an if else statement to print out an arrow 

for i in range(7):
    if i < 5:
        print("*" * (i + 1))
    else:
        print("*" * (8 - i))