print("Select your ride:")
print("1.bike")
print("2.car")
choice=int(input("Enter your choice:  "))
if choice==1:
    print("what type of bike??")
    print("1.Scooter\n")
    print("2.Scooty\n")
    choice2=int(input("Enter your choice no. : "))
    if choice2==1:
        print("You have selected  scooter")
    else:
        print("You have selected scooty")
elif choice==2:
    print("what type of car??")
    print("1.Sedan\n")
    print("2.SUV\n")
    choice3=int(input("Enter your choice no. : "))
    if choice3==1:
        print("You have selected  Sedan")
    else:
        print("You have selected SUV")
else:
    print("WRONG CHOICE!!!")
    


    