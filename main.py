### author: chih-chien Hsiao 2023 copyright
import time

class IDGenerator:
    def __init__(self) -> None:
        self.curIdx = 0
        self.lengthOfID = 8
        self.validIdQueue = []
        self.stack = [("", 0)]
        start_time = time.time()
        self.backtrackingI()
        print("exec time is: " + str(time.time() - start_time) + " secs")

    def GetID(self):
        if self.curIdx >= len(self.validIdQueue):
            self.backtrackingI()
        res = self.validIdQueue[self.curIdx]

        self.curIdx += 1
        return res

    # recursion
    def backtrackingR(self, id:str):
        if len(id) == self.lengthOfID:
            self.validIdQueue.append(id)
            return
        for i in range(0, 10):
            if len(id) > 0 and id[-1] == str(i):
                continue
            id += str(i)
            self.backtrackingR(id)
            id = id[:len(id)-1]

    # iterative (super powerful when you want to stop in the middle of a tree traversal)
    def backtrackingI(self):
        while self.stack:
            if self.curIdx < len(self.validIdQueue):
                return
            curr_id, i = self.stack.pop()
            if len(curr_id) == self.lengthOfID:
                self.validIdQueue.append(curr_id)
            elif i < 10:
                if len(curr_id) > 0 and curr_id[-1] == str(i):
                    self.stack.append((curr_id, i+1))
                else:
                    self.stack.append((curr_id+str(i), 0))
                    self.stack.append((curr_id, i+1))

if __name__ == '__main__':
    idGen = IDGenerator()
    while True:
        print(idGen.GetID())
        name = input("Enter to get next ID")

