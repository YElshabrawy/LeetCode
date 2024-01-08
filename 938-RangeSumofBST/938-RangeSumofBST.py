            sum = 0
            if low <= node.val <= high:
                sum += node.val
                
            sum += doRec(node.left)
            sum += doRec(node.right)
            
            return sum
            
                return 0
            if node is None:
        def doRec(node):
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
class Solution:
[
