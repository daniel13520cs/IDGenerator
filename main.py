import LC106
import Tree
if __name__ == '__main__':
    solution = LC106.Solution106()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    preorder = solution.buildTree(inorder=inorder, postorder=postorder)
    
    bTree = Tree.BinaryTree()
    child = Tree.TreeNode(2)
    bTree.root = Tree.TreeNode()
    bTree.root.left = child
    
    bTree.Print()