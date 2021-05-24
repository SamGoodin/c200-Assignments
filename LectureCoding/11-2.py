#Stack  LIFO (Last In, First Out)
#s = stack()
#Queue
#s.push(23)         [23]
#s.push(45)         [45, 23]
#s.push(67)         [67, 45, 23]
#s.pop() = 67       [45, 23]
#s.empty() True if stack is empty, False if not.

class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.insert(0, x)

    def pop(self):
        if not self.empty():
            g = self.stack[0]
            self.stack.remove(g)
            return g
        else:
            return self

    def empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)

s = "(()(()))"

def balanced(x):
    s = MyStack()
    for i in range(len(x)):
        if x[i] == "(":
            s.push("(")
        elif x[i] == ")":
            s.pop()
    return s.empty()

print(balanced(s))

s = MyStack()
s.push(5)
s.push(10)
s.push(12)
print(s.pop())
print(s)