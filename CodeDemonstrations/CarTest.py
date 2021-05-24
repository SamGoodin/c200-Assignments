from Car import Car

c1 = Car("Toyota", "Camry", 2009)
c2 = Car("Honda", "Accord", 2008)

c1.addAccessory("Radio")
c1.addAccessory("Clock")

print(c1)
print(c2)

c = [c1, c2]
print(c)

for cl in c:
    print(cl, cl.acc)
