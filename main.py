
from tree_traversal import Node, printInorder, printPreorder, printPostorder

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print('INORDER')
printInorder(root)

print('PREORDER')
printPreorder(root)

print('POSTORDER')
printPostorder(root)
