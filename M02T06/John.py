incorrect_names = []

while True:
    name = input("Enter your name: ")
    if name.lower() == "john":
        break  
    incorrect_names.append(name)

print("Incorrect names: ", incorrect_names)


