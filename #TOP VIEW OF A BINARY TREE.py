#TOP VIEW OF A BINARY TREE
class treenode 
def left_view(root):
    if not root:
        return[]
    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for i in range (level_size):
            node = queue.pop(0)
            if i == 0:
                result.append(node.value)

                if node.left:
                    queue.append(node.left)
                    

