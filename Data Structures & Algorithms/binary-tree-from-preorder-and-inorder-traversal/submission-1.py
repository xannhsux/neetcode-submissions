# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder always start with the root
        
        #in inorder everthing on the left side of root is left node
        #we can seperate left branch and right branch by finding root (mid node)

        indices = {val : index for index, val in enumerate(inorder)}
        self.pre_index = 0
        def dfs(l,r):
            if l > r:
                return None
            
            rootVal = preorder[self.pre_index]
            self.pre_index += 1
            root = TreeNode(rootVal)
            mid = indices[rootVal]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder)-1)
