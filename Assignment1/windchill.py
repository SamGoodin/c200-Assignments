temp = float(input("What is the temperature? "))
windV = float(input("What is the wind velocity? "))
twc = 34.74 + (0.6215 * temp) - (35.75 * (windV ** 0.16)) + (0.4275 * temp * (windV ** 0.16))
print(twc)
