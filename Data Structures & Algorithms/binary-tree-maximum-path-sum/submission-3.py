# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        
        #return height 
        def dfs(curr):
            if not curr:
                return 0

            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)
            leftMax = max(0,leftMax)
            rightMax = max(0,rightMax)

            self.res = max(self.res ,curr.val + leftMax + rightMax)
            return curr.val + max(leftMax, rightMax)
        dfs(root)
        return self.res
