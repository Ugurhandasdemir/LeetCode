# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isCousins(self, root, x, y):
        q = deque([(root, None, 0)])  # (node, parent, depth)
        x_info = None  # (parent, depth)
        y_info = None

        while q:
            node, parent, depth = q.popleft()
            if not node:
                continue

            if node.val == x:
                x_info = (parent, depth)
            elif node.val == y:
                y_info = (parent, depth)

            if x_info and y_info:
                break

            q.append((node.left, node, depth + 1))
            q.append((node.right, node, depth + 1))

        if not x_info or not y_info:
            return False

        return (x_info[1] == y_info[1]) and (x_info[0] != y_info[0])