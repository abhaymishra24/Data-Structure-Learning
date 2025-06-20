
# find out Diameter of Binery Tree - 

class Solution(object):
    def diameterOfBinaryTree(self, root):
        # Define a recursive function to calculate the diameter
        def diameter(node, res):
            # Base case: if the node is None, return 0
            if not node:
                return 0
            
            # Recursively calculate the diameter of left and right subtrees
            left = diameter(node.left, res)
            right = diameter(node.right, res)

            # Update the maximum diameter encountered so far
            res[0] = max(res[0], left + right)
            
            # Return the depth of the current node
            return max(left, right) + 1
        
        # Initialize a list to hold the maximum diameter encountered
        res = [0]
        # Call the diameter function starting from the root
        diameter(root, res)
        # Return the maximum diameter encountered
        return res[0]
    
# same code without comments - 

class Solution(object):
    def diameterOfBinaryTree(self, root):

        def dfs(node, res):
            if not node:
                return 0

            left = dfs(node.left, res)
            right = dfs(node.right, res)

            res[0] = max(res[0], left + right)

            return max(left, right) + 1

        res = [0]
        dfs(root, res)

        return res[0]
    
# practice again - 