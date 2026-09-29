# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        Sum = root.val
        def dfs(root): # return the MaxPath without a split 
            nonlocal Sum
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0) # making it 0 if leftMax < 0
            rightMax = max(rightMax, 0)

            # MaxPath with the split 
            Sum = max(Sum, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        dfs(root)
        return Sum
        