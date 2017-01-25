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

