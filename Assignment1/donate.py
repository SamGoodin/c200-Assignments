while 0 < 1:

    bloodType = (input("What is your blood type? ")).lower()
    if bloodType == "a+":
        print("You can donate to A+ or AB+!")
    elif bloodType == "a-":
        print("You can donate to A+, A-, AB+, and AB-!")
    elif bloodType == "b+":
        print("You can donate to B+ or AB+!")
    elif bloodType == "b-":
        print("You can donate to B+, B-, AB+, and AB-!")
    elif bloodType == "ab+":
        print("You can donate to AB+!")
    elif bloodType == "ab-":
        print("You can donate to AB+ and AB-!")
    elif bloodType == "o+":
        print("You can donate to O+, A+, B+, and AB+!")
    elif bloodType == "o-":
        print("You can donate to anyone!")
    else:
        print("That isn't a blood type.")

