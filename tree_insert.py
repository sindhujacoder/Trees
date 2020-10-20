class Node:
  def __init__(self, key):
    self.data = key
    self.left = None
    self.right = None

def insert(root, value):
  if not root:
    root = Node(value)
    return 
  
  q = []
  q.append(root)

  while(q):
    temp = q[0]
    q.pop(0)

    if not temp.left:
      temp.left = Node(value)
      break
    else:
      q.append(temp.left)
    
    if not temp.right:
      temp.right = Node(value)
      break
    else:
      q.append(temp.right)
    

    


