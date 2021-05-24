'''
class MyFirstClass:
    kitty = 1234
    walnut = "Hello, World!"
    
    def foo(self):
        return 43

x = MyFirstClass()

print(x.kitty)
print(x.walnut)
print(x.foo())
'''

class shape:
    
    def __init__(self, loc, l, w):
        self.loc = loc
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def x(self):
        return self.loc[0]

    def y(self):
        return self.loc[1]

    def distance(self, x):
        l = x.x()
        w = x.y()
        return [self.x() - l, self.y() - w]

    def bigger(self, instance):
        if self.area() > instance.area():
            return True
        else:
            return False

s1 = shape([9, 3])
s2 = shape([4, 2])
print(s1.x())
print(s1.y())
print(s1.distance(s2))
