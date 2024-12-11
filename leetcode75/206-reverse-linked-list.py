class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseListIterative(head):
    # NULL -> 1 -> 2 -> 3 -> 4 -> 5
    # NULL <- 1 <- 2 <- 3 <- 4 <- 5
    # O(n) for time, O(1) for space
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def reverseListRecursion(head):
    # O(n) for time, O(n) for space
    def reverse(prev, curr):
        if curr == None:
            return prev
        temp = curr.next  # next
        curr.next = prev
        return reverse(curr, temp)

    return reverse(None, head)
