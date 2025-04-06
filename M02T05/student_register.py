#a program that allows a user to register students for an exam venue 

amount_of_students = int(input("Enter the amount of students you are registering: "))
for i in range(amount_of_students):
    student_id = input("Enter student ID: ")
    with open("reg_form.txt", "a+") as file:
        file.write(student_id + " " + "................." + "\n")
        
