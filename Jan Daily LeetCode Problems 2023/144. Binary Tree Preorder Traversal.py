# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        preOrder = []

        currNode = root

        while currNode != None:
            if currNode.left == None:
                preOrder.append(currNode.val)
                currNode = currNode.right

            else:
                prevNode = currNode.left
                while prevNode.right != None and prevNode.right != currNode:
                    prevNode = prevNode.right

                # create a thread
                if prevNode.right == None:
                    prevNode.right = currNode
                    preOrder.append(currNode.val)
                    currNode = currNode.left

                else:
                    prevNode.right = None
                    currNode = currNode.right
        return preOrder