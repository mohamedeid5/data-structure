# stack

class Stack():
    
    arr = []
    top = -1
    
    def push(self, val):
        if self.top == 4:
            print('stack is full!')
            return
        self.arr.append(val)
        self.top += 1
        
    def pop(self):
        if self.isEmpty():
            print('stack is empty')
            return
        self.arr.pop()
        self.top -= 1
        
    def top_value(self):
        return self.arr[self.top]
        
    def isEmpty(self):
        if not self.arr:
            return True
        
    def print_stack(self):
        for i in range(self.top + 1):
            print(self.arr[i])