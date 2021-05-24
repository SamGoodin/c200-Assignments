''' 
#Inheritence
class Dad:

    def __init__(self):
        pass

    def print(self):
        print("Dad")

    def method(self):
        print("Inheritance")

class Child(Dad):

    def __init__(self):
        #super().__init__()
        Dad.__init__(self)
        self.method()

    def print(self):
        #super().print()
        print("Child")

d = Child()
d.print()
d.method()
'''
'''
#Lambda
def function(a):
    #Stores x within the function
    return lambda x: x + a

f = function(5)
print(f(1))
'''