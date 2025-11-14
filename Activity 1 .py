medical_cause=input("Did you have any medical cause? yes/no: ")
attendance=int(input("Enter the attendance of the student:   "))
if medical_cause== "yes":
    print("You are allowed :) ")
else:
    if attendance>=75:
        print("You are allowed :)")
    else:
        print("You are not allowed :(")
