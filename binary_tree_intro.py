'''
1. The maximum number of nodes at level ‘l’ of a binary tree is 2power(l).
Here level is number of nodes on path from root to the node (including root and node). Level of root is 0

2. Maximum number of nodes in a binary tree of height ‘h’ is 2power(h – 1).

3. In a Binary Tree with N nodes, minimum possible height or minimum number of levels is  ? Log2(N+1)-1

4. Binary Tree with L leaves has at least   ? Log2L ? + 1   levels
'''
class Node:
  def __init__(self, key):
      self.data = key
      self.right = None
      self.left = None

#1.level=0-> max_nodes=2power(l)=2power(0)=1
#2.height=1-> max_nodes=2power(h-1)=2power(0)=1 
#3.N=1-> minimum_level=log2(1+1)-1=1
root = Node(0) 

#1.level=1-> max_nodes=2power(1)=2
#2.height=2-> max_nodes=2power(1)=2
#3.N=2->minium_level=log2(3)-1=1
root.left = Node(1) 
root.right = Node(2) # level 1

#1.level=2-> max_nodes=2power2=4
#2.height=3-> max_nodes=2power(2)=4
#N=4->minium_level=log2(5)-1=1
root.left.left = Node(3)
