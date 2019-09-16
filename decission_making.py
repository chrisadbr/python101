#Monthly attendance tracke
name = input("Enter the name of the student: ")  #prompts user for an input
days_attended = int(input("Enter the number of days attended per month: "))  #number of days attended
total_days = 20

rate = (days_attended / total_days) * 100  #calculating attendance rate
if (days_attended > 0) and (days_attended <= total_days):
#testing attendace rate
    if (rate >= 75) and (rate <= 100):
        print(name + " is allowed to sit for the final exam")

    elif (rate >= 60 ) and (rate < 75):
        print(name.title() + " must report to the instructor before taking the exam")

    elif (rate > 0) and (rate < 60):
        excuse = input("Any doctor note provided (Yes/No): ").lower()
        if excuse == 'yes':
            print(name.title() + " is allowed to take the exam per doctor note")
        else:
            print(name.title() + " must provide written excuse to sit for the exam")

    else:
        print(name.title() + " is not allowed to sit for the exam")

else:
    print("Sorry, " + name.title() + " this is an invalid entry")  #prints a message for an invalid entry
