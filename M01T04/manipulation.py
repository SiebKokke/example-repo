str_manip = input("Please enter a sentence: ")
print(len(str_manip))

last_letter = str_manip[-1]
print(str_manip.replace(last_letter, "@"))

last_three = str_manip[-3:]
print(last_three[-1:-4:-1])

combination_of_front_and_back = str_manip[0:2] + str_manip[-2:]
print(combination_of_front_and_back)