from BodyModule import Sedan, Minivan, Truck

honda1 = Sedan("Honda", "Accord", 2008)
toyota1 = Sedan("Toyota", "Camry", 2009)
silv1 = Truck("Chevrolet", "Silverado", 2001, 3)
m1 = Minivan("Ford", "Windstar", 2002)

olderCar = honda1.olderCar(m1)
print("Older car is:\n" + str(olderCar))

print(honda1)
print(toyota1)
print(silv1)
print(m1)
