# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
              
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                break
        
        current = head
        prev = None
        while current is not None:
            if current.val == val:
                prev.next = current.next
                current = prev.next
            else:
                prev = current
                current = current.next
        
        return head
            
        
                        




        