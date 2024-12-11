class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = f"Value {self.val} pointing to ListNode {self.next}"
        return res


def removeElement(head, val):
    Dummy = ListNode(next=head)
    prev, curr = head, head
    while curr:
        temp = curr.next
        if curr.val == val:
            prev.next = temp
        else:
            prev = curr
        curr = temp
    return Dummy.next


e3 = ListNode(6)
e2 = ListNode(2, e3)
e1 = ListNode(1, e2)
print(removeElement(e1, 6))  # [1,2]

e7 = ListNode(6)
e6 = ListNode(5, e7)
e5 = ListNode(4, e6)
e4 = ListNode(3, e5)
e3 = ListNode(6, e4)
e2 = ListNode(2, e3)
e1 = ListNode(1, e2)
head = [1, 2, 6, 3, 4, 5, 6]
val = 6
print(removeElement(e1, val))  # [1,2,3,4,5]
