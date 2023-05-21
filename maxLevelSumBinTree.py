class Solution:

    def Sum(self, queue):
        sum = 0
        for node in queue:
            sum += node.val
        return sum

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSums = []
        myQueue = [root]
        nextQueue = []

        while(myQueue):
            levelSums.append(self.Sum(myQueue))
            for node in myQueue:
                if node.left: nextQueue.append(node.left)
                if node.right: nextQueue.append(node.right)
            myQueue = nextQueue.copy()
            nextQueue.clear()
        return(1 + levelSums.index(max(levelSums)))