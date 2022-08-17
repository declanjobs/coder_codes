from collections import deque

from Lintcode import TreeNode

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here

        serial = []
        serial_layer = []
        q = deque([(root, 0)])
        non_empty = set()

        while q:

            temp, layer = q.popleft()

            if len(serial_layer) < layer+1:
                if (layer-1) in non_empty:
                    serial += serial_layer[layer-1]
                serial_layer.append([])

            if not temp:
                serial_layer[layer].append("#")
                continue

            non_empty.add(layer)
            serial_layer[layer].append(str(temp.val))

            q.append((temp.left,  layer+1))
            q.append((temp.right, layer+1))

        #print(serial)

        return "{" + ",".join(serial) + "}"


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

        data = data[1:-1].split(",")

        #print(data)
        if not data or data[0] == "":
            return None

        data = deque(data)
        head = TreeNode(int(data.popleft()))

        q = deque([head])

        isLeft = True
        while data:

            val = data.popleft()

            if val == "#":
                pass
            else:

                node = TreeNode(int(val))

                q.append(node)

                if isLeft:
                    q[0].left = node
                else:
                    q[0].right = node

            if not isLeft:
                q.popleft()

            isLeft = not isLeft

        return head

