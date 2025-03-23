# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n) since we traverse the singly-linked list once
        # Space: O(1) since we use the node variable to keep track of the current node
        node = head
        while node and node.next:
            # if duplicate is found, skip the duplicate to point at the next node
            if node.val == node.next.val:
                node.next = node.next.next
            # if there is no duplicate, move on to the next node
            else:
                node = node.next
        return head
