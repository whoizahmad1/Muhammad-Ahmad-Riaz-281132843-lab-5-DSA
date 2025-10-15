class Node:
    """
    A node class for circular linked list.
    Each node contains data and a pointer to the next node.
    """
    
    def __init__(self, data):
        """
        Initialize a new node with given data.
        
        Args:
            data: The value to be stored in the node
        """
        self.data = data
        self.next = None