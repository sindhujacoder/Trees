'''
           1
          /  \
        /     \
      2        3
     / \
    /   \
  4      5
Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
    Uses of Inorder
    In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal s reversed can be used.

(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Breadth First or Level Order Traversal : 1 2 3 4 5

All four traversals require O(n) time as they visit every node exactly once.

Extra Space required for Level Order Traversal is O(w) where w is maximum width of Binary Tree. In level order traversal, queue one by one stores nodes of different level.
Extra Space required for Depth First Traversals is O(h) where h is maximum height of Binary Tree. In Depth First Traversals, stack (or function call stack) stores all ancestors of a node.
'''

class Node:
  def __init__(self, key):
    self.data = key
    self.left = None
    self.right = None
  
def printInorder(root):
  if root:
    printInorder(root.left)
    print(root.data)
    printInorder(root.right)
  
def printPreorder(root):
  if root:
    print(root.data)
    printPreorder(root.left)
    printPreorder(root.right)
  
def printPostorder(root):
  if root:
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.data)

