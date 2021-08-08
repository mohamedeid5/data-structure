# main

class Queue():
    
    capcity = 1000
    arr = [None] * capcity
    front = rear = -1
    
    def enqueue(self, val):
        if self.isFull():
            print('queue is full')
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear += 1
        self.arr[self.rear] = val
        
    def dequeue(self):
        if self.isEmpty():
            print('queue is empty')
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
    
    def isEmpty(self):
        if self.rear == -1 and self.rear == -1:
            return True
        else:
            return False
        
    def isFull(self):
        if self.rear == self.capcity - 1:
            return True
        else:
            return False
        
    def front_value(self):
        if self.isEmpty():
            return 'queue is empty'
        return self.arr[self.front]
    
    def print_queue(self):
        for i in range(self.front, self.rear + 1):
            print(self.arr[i])
    



    