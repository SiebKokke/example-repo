time_swim = int(input("enter your triathlon time in minutes for the swimming portion: "))
time_cycle = int(input("enter your triathlon time in minutes for the cycling portion: "))
time_run = int(input("enter your triathlon time in minutes for the running portion: "))

total_time = time_swim + time_cycle + time_run

print("was your total triathlon time was", total_time, "minutes")
if total_time <= 100:
    print("Within the qualifying time, Award: provincial colours")
elif total_time > 100 and total_time <= 105:
        print("five minutes off from the qualifying time, Award: provincial half colours")
elif total_time > 105 and total_time <= 110:
        print("10 minutes off from the qualifying time, Award: provinicial scroll")
else:
    print("more than 10 minutes off from the qualifying time, no award")
