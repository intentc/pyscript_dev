class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        self.__list.append(item)
        # print(self.item)

    def dequeue(self):
        self.__list.pop(0)

#    def pri(self):
#        print(self.__list)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # 1
print(q.dequeue())  # 2
print(q.dequeue())  # 3

#q.pri()