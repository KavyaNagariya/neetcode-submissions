# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # First we will check whether the root or subroot is null or not 
        if not subRoot:
            return True # subroot exist nhi karega matlab root ho ya nhi subtree hoga hi hoga
        if not root:
            return False # Baad me ise check karenge agar subRoot hai lekin root nhi to False

        if self.sameTree(root, subRoot):
            return True  # pehle check kro if root == subRoot 
    
        # then check kro ye subtree to nhi hai left ya right ka 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return (self.sameTree(root1.left, root2.left) and 
                    self.sameTree(root1.right, root2.right))
        return False
