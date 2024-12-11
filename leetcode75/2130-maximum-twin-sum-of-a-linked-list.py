class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head):
    # set up to divide into two link list
    sHead = head
    slow = head
    fast = head.next
    while fast.next:
        slow = slow.next
        fast = fast.next.next
    fHead = slow.next
    slow.next = None

    # reverse the second half link list
    prev = None
    curr = fHead
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    # traverse two link list to find the maximum twin sum of the original link list
    s = sHead
    fHead = fast
    f = fHead
    maxSoFar = 0
    while s or f:
        maxSoFar = max(maxSoFar, s.val + f.val)
        s = s.next
        f = f.next
    return maxSoFar


e8 = ListNode(7)
e7 = ListNode(6, e8)
e6 = ListNode(5, e7)
e5 = ListNode(4, e6)
e4 = ListNode(3, e5)
e3 = ListNode(6, e4)
e2 = ListNode(2, e3)
e1 = ListNode(1, e2)
print(pairSum(e1))
