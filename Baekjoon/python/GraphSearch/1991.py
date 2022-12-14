from collections import defaultdict

n = int(input())

tree = defaultdict(list)
for _ in range(n):
    parent, child1, child2 = map(str, input().split())
    tree[parent].append(child1)    
    tree[parent].append(child2)

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')