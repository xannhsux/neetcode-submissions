# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        #the node that the whole group is pointing to 
        #after reversed
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            #if no enough nodes
            if not kth:
                break
            # 1 2 3 4 k=3 groupNext = 4th node 
            groupNext = kth.next
            
            #start reversing group
            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr