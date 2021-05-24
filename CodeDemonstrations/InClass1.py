#Create a program to give opinion on input color

while 0 < 1:
    color = (input("What is your favorite basic color? ")).lower()
    if color == "red" or color == "blue" or color == "yellow":
        print("That is a primary color.")
    elif color == "black" or color == "white":
        print("That color is basic.")
    elif color == "orange" or color == "green" or color == "purple" or color == "violet":
        print("That is a secondary color.")
    elif color == "brown":
        print("Brown is a composite color.")
    else:
        print("I don't understand what color that is.")

