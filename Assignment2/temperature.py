celcTemp = int(input("What is the temperature in Celcius? "))

def conversion(temperature):
    return temperature * (9/5) + 32

fTemp = conversion(celcTemp)
if fTemp < 45:
    print("Wear a coat!")
elif fTemp > 90:
    print("Stay hydrated!")
