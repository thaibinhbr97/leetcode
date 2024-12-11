class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow, fast = head, head
    while fast:
        slow = slow.next
        fast = fast.next.next
    return slow
