#asks user a number, -1 stops the program, 0 is not a valid number

#we need to initialize the variables to 0
number = 0
count = 0
total = 0 

while number != -1:
    number = int(input("Enter a number: "))
    print(number)
    
    if number == 0:
        print("0 is not a valid number")
        continue
    if number == -1:
        print("-1 stops the program")
        break

#we need to add the number to the total and increase the count
    total += number
    count += 1

if count > 0:
    print("The average is", total / count)


