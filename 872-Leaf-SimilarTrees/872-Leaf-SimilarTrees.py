

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = getSequence(root1)
        seq2 = getSequence(root2)
        return seq1 == seq2


        
[
