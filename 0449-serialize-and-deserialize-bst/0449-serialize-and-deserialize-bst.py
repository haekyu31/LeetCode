# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        path_of_preorder = []
        def helper( node ):
            
            if node:
                path_of_preorder.append( node.val )
                helper( node.left )
                helper( node.right )
        helper( root )
        return '#'.join( map(str, path_of_preorder) )
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        node_values = deque(  int(value) for value in data.split('#') )
        
        def helper( lower_bound, upper_bound):
            
            if node_values and lower_bound < node_values[0] < upper_bound:
                
                root_value = node_values.popleft()
                root_node = TreeNode( root_value )
                
                root_node.left = helper( lower_bound, root_value )
                root_node.right = helper( root_value, upper_bound )
                
                return root_node
            
        return helper( float('-inf'), float('inf'))
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans