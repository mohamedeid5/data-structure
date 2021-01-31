class Stack:
    arr = []
    top = -1

    def push(self, val):
        if self.top == 1000:
            print('array is full')
        else:
            self.arr.append(val)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            return 'array is empty'
        self.arr.pop()
        self.top -= 1

    def topValue(self):
        if self.isEmpty():
            return 'stack is empty'
        return self.arr[self.top]

    def isEmpty(self):
        if not self.arr:
            return True

    def printStack(self):
        for i in range(self.top + 1):
            print(self.topValue())
            self.pop()






