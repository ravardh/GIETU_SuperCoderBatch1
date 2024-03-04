class AVLNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 0

class AVLTree:
    def insert(self, root, value):
        if root is None:
            return AVLNode(value)
        if value < root.data:
            root.left = self.insert(root.left, value)
        elif value > root.data:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance_factor = self.get_balance(root)

        if balance_factor > 1 and value < root.left.data:
            return self.right_rotate(root)
        elif balance_factor < -1 and value > root.right.data:
            return self.left_rotate(root)
        elif balance_factor > 1 and value > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        elif balance_factor < -1 and value < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y):
        z = y.left
        T3 = z.right

        z.right = y
        y.left = T3

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))

        return z

    def level_order(self, root):
        if root is None:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None
    value_list = [50, 45, 55, 35, 40, 48, 60, 20, 70, 41, 47, 42, 15, 22, 25, 30, 90]

    for value in value_list:
        root = avl_tree.insert(root, value)

    print("Level Order traversal of the AVL tree:")
    avl_tree.level_order(root)
