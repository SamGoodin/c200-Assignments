# y = mx + b
# m is slope rate of change outputs/inputs delta y / delta x

def f(x, m, b):
    y = m * x + b
    return y

#1 given m, b

#2 p1 = (x1, y1) p2 = (x2, y2)
    # m = (y2 - y1) / (x2 - x1) = (y1 - y2) / (x1 - x2)
    # m = (y - y2) / (x - x2) => mx - mx2 = y - y2 => mx - mx2 + y2 = y

import matplotlib.pyplot as plt

class MyLine:

    def __init__(self, p1, p2):
        # p1 = [x11, x12] p2 = [x21, y21]
        self.p1 = p1
        self.p2 = p2
        self.m = (p2[1] - p1[1]) / (p2[0] - p1[0])
        self.b = p1[1] - self.m * p1[0]
        self.line = lambda x: (self.m * x) + self.b

    def apply_f(self, x):
        return self.line(x)

    def line_from_point_slope(self, m, p):
        b = p[1] - m * p[0]
        return lambda x: (m * x) + b

    def draw(self):
        x1, y1 = [1, 32], [4, 10]
        x2, y2 = [3, 30], [10, 5]
        plt.plot(x1, y1, x2, y2, marker = '.')
        plt.plot(18, 7.1, marker = 's')
        plt.show()

x1 = MyLine([0, 0], [4, 3])
print(x1.apply_f(3))
print(x1.line_from_point_slope((3/4), [0, 0])(3))
x1.draw()
