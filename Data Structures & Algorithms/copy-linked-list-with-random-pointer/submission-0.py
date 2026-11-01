"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyToNew = {}
        cur = head

        while cur:
            copyToNew[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = copyToNew.get(cur)
            copy.next = copyToNew.get(cur.next)
            copy.random = copyToNew.get(cur.random)

            cur = cur.next
        return copyToNew.get(head)