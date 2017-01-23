# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:48:26 2017

@author: sominwadhwa

A basic linked list
"""

class Node(object):
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.data)
        

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self,data):
        if not self.head:
            node = Node(data)
            self.head = node
        else:
            node = self.head
            while (node.next != None):
                node = node.next
            new_node = Node(data)
            node.next = new_node
            new_node.prev = node
            return
    def appendAfterKey(self, data, pos):
        p = 1
        node = self.head
        while (p<pos):
            node = node.next
            p+=1
        new_node = Node(data)
        node.next.prev = new_node
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
    def delete(self, d):
        if (self.head.data == d):
            self.head = self.head.next
        else:
            current = self.head
            while (current.next != None and current.data != d):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
    def printList(self):
        node = self.head
        while (node):
            print (str(node))
            node = node.next

newList = LinkedList()
newList.append(1)
newList.append(2)
newList.append(3)
newList.append(4)
newList.append(5)
newList.append(6)
newList.appendAfterKey(36,3)
newList.delete(3)
newList.printList()

