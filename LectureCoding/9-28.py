'''
print("kit" + "ty")
print("kit", "ty")
#Error
#print("kit" + 3)
print("kit" + str(3))
print("kit", 3)
'''

for i in range(0, 4):
    print("i={0}".format(i))
    #Removes curly brackets when printing

print(5 * "{0} sees {1} {2} on the court.".format("Sam", "Lebron James", "flop"))

x = [3, 1, 7]
y = str(x)
print(y[0])