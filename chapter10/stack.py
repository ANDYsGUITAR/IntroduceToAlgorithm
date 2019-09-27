class Stack(object):
    def __init__(self):
        self.data = []
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def push(self, val):
        self.data.append(val)
        self.top += 1

    def pop(self):
        if self.top < 0:
            print("The stack has not any element")
            return None
        self.top -= 1
        return self.data.pop(-1)

my_stack = Stack()
print(my_stack.isEmpty())
my_stack.push(1)
print(my_stack.isEmpty())
print(my_stack.pop())
print(my_stack.isEmpty())
