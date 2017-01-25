class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return (self.data)

class Stack(object):
    def __init__(self):
        self.top = None
    def push(self,data):
        if (self.top == None):
            node = Node(data)
            self.top = node
        else:
            node = Node(data)
            node.next = self.top
            self.top = node
    def pop(self):
        if (self.top == None):
            return ("Underflow")
        else:
            item = self.top.data
            self.top = self.top.next
            return item 
    def peek(self):
        item = self.top.data
        return item
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print (stack.pop())
    print (stack.peek())
