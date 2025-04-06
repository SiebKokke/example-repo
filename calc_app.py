#ask user to perform a calculation or print previous calculations
#ask user for the first number
#ask user for the second number
#ask user for the operation
#perform the calculation
#and display the answer

while True:
    choice = input("Do you want to perform a calculation or print all the previous calcultions? (calculation or print): ").lower()
    if choice == "calculation":
        try:
            first_num = int(input("Enter the first number: "))
            second_num = int(input("Enter the second number: "))
            operation = input("Enter the operation(+, -. *, or /): ")

            if operation == "+":    
                    calculation = first_num + second_num                
            elif operation == "-":
                    calculation = first_num - second_num
            elif operation == "*":
                    calculation = first_num * second_num
            elif operation == "/":
                    calculation = first_num / second_num
                    if second_num == 0:
                        print("Cannot divide by zero")
                        calculation = "Cannot divide by zero"
                    else:
                        calculation = first_num / second_num
            else:
                print("Invalid operation")
                calculation = "Invalid operation"
        
        except ValueError:
            print("Invalid input, please try again and enter a number or a valid operation")
            calculation = "Invalid input"
    
    
        #store the calculation in a file called equations.txt        
        with open("equations.txt", "a+") as file:
            file.write(f"{first_num} {operation} {second_num} = {calculation}\n")
            print("The answer is", calculation)

    elif choice == "print":
        try:
            with open("equations.txt", "r") as file:
                for line in file:
                    print(line)
        except FileNotFoundError:
            print("No calculations have been made yet")
    else:
        print("Invalid choice, please enter print or calculation")
       

#use defensive programming in case an error occurs during the calculation or while printing the file 

