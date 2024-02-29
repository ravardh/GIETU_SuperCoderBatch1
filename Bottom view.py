class Pair:
    
    def __init__(self, root, level):
        self.root = root
        self.level = level
        
	
def bottomView(root):
    horizontalDistance = 0
    mp = OrderedDict()
    
    q = []
    
    p1 = Pair(root, 0)
    q.append(p1)
    
    while len(q) > 0:
        p = q.pop(0)
        
        mp[p.level] = p.root
        
        if p.root.left is not None:
            q.append(Pair(p.root.left, p.level - 1))
            
        if p.root.right is not None:
            q.append(Pair(p.root.right, p.level + 1))
            
    bottomViewList = []
    
    for key in mp.keys():
        bottomViewList.append(key)
        
        
    bottomViewList.sort()
    
    for i in bottomViewList:
        print(mp.get(i).data, end = “ ”)
