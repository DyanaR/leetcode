import sys

class Node:
    def __init__(self, data):
        # The 'next' attribute is initialized to None by default because a new node
        # does not need to be linked to another node at the time of creation. 
        # This keeps node creation simple and allows links to be set later when needed.
        self.data = data
        self.next = None
        

def main():
    # grab value from user
    node1 = Node(sys.argv[1])
    node2 = Node(sys.argv[2])
    node3 = Node(sys.argv[3])
    node4 = Node(sys.argv[4])
    
    # link the nodes using next pointers
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    currentNode = node1
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")
    
main()