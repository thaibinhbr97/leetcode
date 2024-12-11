class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = f"Value {self.val} pointing to ListNode {self.next}"
        return res

    def getVal(self):
        return self.val


def oddEvenList(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    evenHead = head.next
    while even and even.next:
        odd.next = even.next
        odd = even.next
        even.next = odd.next
        even = odd.next
    odd.next = evenHead
    return head


e7 = ListNode(6)
e6 = ListNode(5, e7)
e5 = ListNode(4, e6)
e4 = ListNode(3, e5)
e3 = ListNode(6, e4)
e2 = ListNode(2, e3)
e1 = ListNode(1, e2)
print(oddEvenList(e1))
