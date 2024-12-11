class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        # Dummy node
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index):
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1  # index out of bound

    def insertHead(self, val):
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            # if list was empty before inserting
            self.tail = newNode
        return

    def insertTail(self, val):
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index):
        i = 0
        curr = self.head
        while curr and i < index:
            # move curr to  node before target node
            curr = curr.next
            i += 1
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self):
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
