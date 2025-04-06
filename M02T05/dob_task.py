#create two lists, first of the names and the second of the DOBs 

lines = []

#retrieve data from the file
with open("DOB.txt", "r") as file:
    for line in file:
        lines.append(line)

#initialize lists
names = []
dob = []

for line in lines:
    parts = line.split(" ") 
    if len(parts) >= 4:
        name =  " ".join(parts[:-3])   
        date_of_birth = " ".join(parts[-3:])
        
        names.append(name)
        dob.append(date_of_birth.strip())

print("names:")
for name in names:
    print(name)

print("\nbirthdate:")
for date in dob:
    print(date)