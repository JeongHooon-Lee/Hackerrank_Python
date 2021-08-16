#https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem?h_r=next-challenge&h_v=zen

def insertNodeAtTail(head, data):
        node = SinglyLinkedListNode(data)
        a
        if not head:
            head=node
            return head
        else:
            current=head
            while(current.next):
                current=current.next
            current.next=node
        return head