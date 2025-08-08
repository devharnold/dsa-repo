#1448 - Count Good Nodes in Binary Tree

# Definition of a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count_nodes(root, root.val)
    
    def count_nodes(self, curr_min, node) -> int:
        if not node:
            return 0
        
        # find the maximum value in the path
        max_val = max(curr_min, node.val)
        r = 0 # initialize root to 0, youll then increment by one if the node value is greater than the current minimum
        if node.val >= curr_min:
            r += 1

        return self.count_nodes(node.left, max_val) + self.count_nodes(node.right, max_val) + r