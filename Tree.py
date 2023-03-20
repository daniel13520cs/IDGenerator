from curses import update_lines_cols
from typing import List, Optional
import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class BinaryTree:
    def __init__(self, root:TreeNode=None) -> None:
        self.root = None
        self.level = 0
        self.q = queue.Queue()
        self.levelMap = {}
        
    def Print(self) -> None:
        print(self.Serialize())
        print(self.levelMap)
    
    def Serialize(self) -> List[int]:
        if self.root:
            self.q.put(self.root)
        res = []
        lvl = 0
        next = queue.Queue()
        while not self.q.empty():
            self.levelMap[lvl] = self.q
            while not self.q.empty():
                cur = self.q.get()
                if cur:
                    next.put(cur.left)
                    next.put(cur.right)
                res.append(cur.val if cur else -1)
            lvl += 1
            self.q = next
        return res
            
    def Deserialize(self, input:List[TreeNode]) -> None:
        if len(input) == 0:
            return
        