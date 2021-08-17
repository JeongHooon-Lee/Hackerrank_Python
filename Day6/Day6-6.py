#https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
#이퀄때문에 햇갈린문제
#!/bin/python3
import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    # Write your code here
    node=DoublyLinkedListNode(data)
    if node.data < llist.data:
        node.next=llist
        llist.prev=node
        llist=node
        return llist
    else:
        cur=llist
        while True:
            if cur.next == None:
                cur.next=node
                return llist
            elif cur.data <= node.data and cur.next.data >= node.data:
                cur.next.prev=node
                node.next=cur.next
                node.prev=cur
                cur.next=node
                return llist
            cur=cur.next

if __name__ == '__main__':