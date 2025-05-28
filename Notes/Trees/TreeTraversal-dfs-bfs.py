# create node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BFS: level order traversal - FIFO
def bfs(root):
    if root is None:
        return
    # use a queue to keep track of what nodes to visit next
    # starting w root node
    queue = [root]
    while queue: # as long as there are nodes in the queue
        node = queue.pop(0) # take node out
        print(node.data, end=' ')
        # check if children exist and add them to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Pre-Order DFS: root, left, right
def pre_order_dfs(node):
    if node is None:
        return
    print(node.data, end=' ')
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)
    
# In-Order DFS: left, root, right
def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data, end=' ')
    in_order_dfs(node.right)
    
# Post-Order: left, right, root
def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.data, end=' ')

if __name__ == "__main__":
    # create tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
            
    #         2
    #        / \
    #       3   4
    #      /
    #     5
    
    print("BFS: ", end='')
    bfs(root)
    print("\nPre Order DFS: ", end='')
    pre_order_dfs(root)
    print("\nIn Order DFS: ", end='')
    in_order_dfs(root)
    print("\nPost Order DFS: ", end='')
    post_order_dfs(root)
    