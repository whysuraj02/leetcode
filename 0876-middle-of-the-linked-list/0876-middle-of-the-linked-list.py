# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        # curr = head
        # len_ll = 0
        # while curr:
        #     len_ll += 1
        #     curr = curr.next
        
        # current = head
        # for _ in range(len_ll//2):
        #     current = current.next
        # return current

        s = head
        h = head
        while h != None and h.next != None:
            s = s.next
            h = h.next.next
        return s



        
        

        

        


        