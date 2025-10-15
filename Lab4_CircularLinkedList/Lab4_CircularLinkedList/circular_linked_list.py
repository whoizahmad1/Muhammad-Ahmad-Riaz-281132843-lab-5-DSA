from node import Node


class CircularLinkedList:
    """
    A circular linked list implementation.
    In a circular linked list, the last node points back to the first node.
    """
    
    def __init__(self):
        """
        Initialize an empty circular linked list.
        """
        self.head = None
    
    def insert_end(self, data):
        """
        Insert a new node at the end of the circular linked list.
        
        Args:
            data: The value to be inserted
        """
        new_node = Node(data)
        
        if self.head is None:
            # If list is empty, make the new node the head and point to itself
            self.head = new_node
            new_node.next = self.head
        else:
            # Find the last node (the one that points to head)
            current = self.head
            while current.next != self.head:
                current = current.next
            
            # Insert the new node at the end
            current.next = new_node
            new_node.next = self.head
    
    def insert_begin(self, data):
        """
        Insert a new node at the beginning of the list.
        
        Args:
            data: The value to be inserted
        """
        new_node = Node(data)
        
        if self.head is None:
            # If list is empty, make the new node the head and point to itself
            self.head = new_node
            new_node.next = self.head
        else:
            # Find the last node to update its next pointer
            current = self.head
            while current.next != self.head:
                current = current.next
            
            # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
            current.next = self.head  # Update the last node's next pointer
    
    def insert_after(self, target, data):
        """
        Insert a new node after a node with a specific value (target).
        
        Args:
            target: The value after which to insert the new node
            data: The value to be inserted
        """
        if self.head is None:
            print("List is empty. Cannot insert after target.")
            return
        
        new_node = Node(data)
        current = self.head
        
        # Find the target node
        while True:
            if current.data == target:
                # Insert after the target node
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                # We've gone full circle and didn't find the target
                print(f"Target value {target} not found in the list.")
                return
    
    def delete_node(self, key):
        """
        Delete the first node that contains the given key.
        
        Args:
            key: The value of the node to be deleted
        """
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        
        # Case 1: Only one node in the list
        if self.head.next == self.head and self.head.data == key:
            self.head = None
            return
        
        # Case 2: Delete head node
        if self.head.data == key:
            # Find the last node
            last = self.head
            while last.next != self.head:
                last = last.next
            
            # Update head and last node's next pointer
            self.head = self.head.next
            last.next = self.head
            return
        
        # Case 3: Delete a node that is not the head
        current = self.head
        while current.next != self.head:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
        
        print(f"Node with value {key} not found in the list.")
    
    def search(self, key):
        """
        Return True if a node with value key exists; otherwise, return False.
        
        Args:
            key: The value to search for
            
        Returns:
            bool: True if key is found, False otherwise
        """
        if self.head is None:
            return False
        
        current = self.head
        while True:
            if current.data == key:
                return True
            current = current.next
            if current == self.head:
                break
        
        return False
    
    def reverse(self):
        """
        Reverse the entire circular linked list so the last becomes the first.
        """
        if self.head is None or self.head.next == self.head:
            # List is empty or has only one node
            return
        
        # Store the original head
        original_head = self.head
        
        # Find the last node
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        
        # Break the circular link temporarily
        last_node.next = None
        
        # Reverse the list
        prev = None
        current = original_head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Update head and make it circular again
        self.head = prev
        original_head.next = self.head
    
    def display(self):
        """
        Print all elements in a readable format.
        """
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        elements = []
        
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        print(" -> ".join(elements) + " -> (back to head)")
    
    def count_nodes(self):
        """
        Return the total number of nodes in the list.
        
        Returns:
            int: Number of nodes in the list
        """
        if self.head is None:
            return 0
        
        count = 0
        current = self.head
        
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        
        return count
    
    def clear(self):
        """
        Remove all nodes (make the list empty).
        """
        self.head = None