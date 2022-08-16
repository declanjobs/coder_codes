"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return ['#']
        q = [root]
        ans = []
        while q:

            temp = q.pop(0)

            if not temp:
                ans.append('#')
            else:
                ans.append(temp.val)
                q.append(temp.left)
                q.append(temp.right)

        return ans

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here

        if not len(data) or data[0] == '#':
            return None

        root = TreeNode(int(data.pop(0)))

        q = [root]

        isLeft = True

        while data:
            temp = data.pop(0)

            if temp == '#':

                pass

            else:
                node = TreeNode(int(temp))

                q.append(node)

                if isLeft:

                    q[0].left = node
                else:
                    q[0].right = node

            if not isLeft:
                q.pop(0)

            isLeft = not isLeft



        return root

