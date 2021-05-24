speed = int(input("What is your speed? "))
minutes = int(input("How many minutes have you travelled for? "))

def myDistance(speed, time):
    miles = speed * (time/60)
    return miles

print(myDistance(speed, minutes))

miles = int(input("How many miles have you travelled? "))
hours = int(input("How many hours have you travelled for? "))

def mySpeed(distance, time):
    speed = distance * time
    return speed

print(mySpeed(miles, hours))
