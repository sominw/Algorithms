class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return (self.data)

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
    def insert(self,data):
        node = Node(data)
        if (self.last != None):
            self.last.next = node
        self.last = node
        if (self.first == None):
            self.first = self.last
    def remove(self):
        if (self.first == None):
            return ("Underflow")
        else:
            item = self.first.data
            self.first = self.first.next
            return item
    def peek(self):
        if (self.first == None):
            return ("Underflow")
        else:
            item = self.first.data
            return item

if __name__=='__main__':
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)
    queue.insert(5)
    print (queue.remove())
    print (queue.remove())
    print (queue.remove())
    print (queue.remove())
    print (queue.remove())
    print (queue.remove())
