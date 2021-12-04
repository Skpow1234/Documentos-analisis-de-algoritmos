class Cola:
    def __init__(self,n):
        self.head = 1
        self.tail = 1
        self.cola = [None]*n
        self.size = n

    def enqueue(self,x):
        if self.head == self.tail and self.cola.count(None)==0:
            return "Overflow"
        else:
            self.cola[self.tail-1] = x
            self.tail+=1
            if self.tail > self.size:
                self.tail = 1
    
    def dequeue(self):
        if self.head == 1 and self.tail == 1 and self.cola.count(None)==self.size:
            return "Underflow"
        else:
            a = self.cola[self.head-1] 
            self.cola[self.head-1] = None
            self.head+=1
            if self.head > self.size:
                self.head = 1
            return a
"""
cola = Cola(5)
cola.enqueue(5)
print(cola.cola)
cola.enqueue(8)
print(cola.cola)
cola.enqueue(10)
print(cola.cola)
print(cola.dequeue())
print(cola.cola)
print(cola.dequeue())
print(cola.cola)
print(cola.enqueue(20))
print(cola.cola)
"""    