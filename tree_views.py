from collections import defaultdict, deque
class node:
    def __init__(self,info=None):
        self.data=info
        self.left=None
        self.right=None
def left_view(root, level, max_level):
    if root is None:
        return
    if level > max_level[0]:
        print(root.data, end=" ")
        max_level[0] = level
    left_view(root.left, level + 1, max_level)
    left_view(root.right, level + 1, max_level)

def right_view(root, level, max_level):
    if root is None:
        return
    if level > max_level[0]:
        print(root.data, end=" ")
        max_level[0] = level

    right_view(root.right, level + 1, max_level)
    right_view(root.left, level + 1, max_level)

def top_view(root):
    if root is None:
        return

    hd_map = defaultdict(int)
    queue = deque([(root, 0)])  # Tuple of (node, horizontal distance)

    while queue:
        node, hd = queue.popleft()

        if hd not in hd_map:
            hd_map[hd] = node.data
            print(node.data, end=" ")

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

def bottom_view(root):
    if root is None:
        return

    hd_map = dict()
    queue = deque([(root, 0)])  # Tuple of (node, horizontal distance)

    while queue:
        node, hd = queue.popleft()

        hd_map[hd] = node.data

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    for hd in sorted(hd_map):
        print(hd_map[hd], end=" ")

root=node(9)
root.left=node(7)
root.right=node(1)
root.left.left=node(6)
root.left.right=node(4)
root.left.left.right=node(5)
root.right=node(1)
root.right.left=node(3)
root.right.left.left=node(11)
root.right.right=node(2)
root.right.left.right=node(12)
root.right.left.right.right=node(17)

max_level = [0]
print("Left View:")
left_view(root, 1, max_level)

max_level = [0]
print("\nRight View:")
right_view(root, 1, max_level)

print("\nTop View:")
top_view(root)

print("\nBottom View:")
bottom_view(root)


