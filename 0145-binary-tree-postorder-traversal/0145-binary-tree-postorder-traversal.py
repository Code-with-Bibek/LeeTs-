class Solution(object):
    def postorderTraversal(self, root):
        result = []
        def visit(node):
            if not node:
                return
            visit(node.left)

            visit(node.right)

            result.append(node.val)
        visit(root)
        return result