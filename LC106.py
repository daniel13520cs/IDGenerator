from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution106:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        postMap = {}
        for i, num in enumerate(inorder):
            inMap[num] = i
        for i, num in enumerate(postorder):
            postMap[num] = i
        def buildTreeHelper(inLeft:int, inRight:int, postLeft:int, postRight:int):
            if inLeft > inRight or (postLeft > postRight):
                return None
            if inLeft == inRight or (postLeft == postRight):
                return TreeNode(inorder[inLeft])
            rootVal = postorder[postRight]
            root = TreeNode(rootVal)
            inRootIdx = inMap[rootVal]
            numsOfLeft = inRootIdx - inLeft - 1
            root.left = buildTreeHelper(inLeft, inLeft + numsOfLeft, postLeft, postLeft + numsOfLeft)
            root.right = buildTreeHelper(inRootIdx + 1, inRight, postLeft + numsOfLeft + 1, postRight - 1)
            return root
        return buildTreeHelper(0, len(inorder) - 1, 0, len(postorder) - 1)

