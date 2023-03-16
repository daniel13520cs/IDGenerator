import LC106
if __name__ == '__main__':
    solution = LC106.Solution106()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    preorder = solution.buildTree(inorder=inorder, postorder=postorder)
    