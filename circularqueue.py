class Queue:

    def __init__(self):
        self.capacity = 5
        self.arr = []
        self.front = self.rear = -1

    def enqueue(self, val):
        if self.isFull():
            print('queue is full!')
        elif self.isEmpty():
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.arr.append(val)

    def dequeue(self):
        if self.isEmpty():
            return
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False

    def isFull(self):
        if (self.rear + 1) % self.capacity == self.front:
            return True
        else:
            return False

    def front_val(self):
        return self.arr[self.front]

    def printQueue(self):
        for i in range(self.front, self.rear + 1):
            print(self.arr[i])


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)


queue.printQueue()

