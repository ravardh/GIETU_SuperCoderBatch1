
from collections import deque

class Node:
	
	def __init__(self, key):
		
		self.data = key
		self.hd = float('inf')
		self.left = None
		self.right = None

def bottomView(root):

	if (root == None):
		return

	hd = 0

	min_hd, max_hd = 0, 0
	
	hd_dict = dict()

	q = deque()

	root.hd = hd
	q.append(root) 

	while q:
		curr_node = q.popleft()

		hd = curr_node.hd

		min_hd = min(min_hd, hd)
		max_hd = max(max_hd, hd)

		hd_dict[hd] = curr_node.data

		if curr_node.left:
			curr_node.left.hd = hd - 1
			q.append(curr_node.left)


		if curr_node.right:
			curr_node.right.hd = hd + 1
			q.append(curr_node.right)


	for i in range(min_hd, max_hd+1):
		print(hd_dict[i], end = ' ')

if __name__=='__main__':
	
	root = Node(20)
	root.left = Node(8)
	root.right = Node(22)
	root.left.left = Node(5)
	root.left.right = Node(3)
	root.right.left = Node(4)
	root.right.right = Node(25)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)
	
	print("Bottom view of the given binary tree :")
	
	bottomView(root)

