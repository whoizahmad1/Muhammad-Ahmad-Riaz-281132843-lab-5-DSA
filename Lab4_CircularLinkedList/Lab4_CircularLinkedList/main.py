from circular_linked_list import CircularLinkedList


def main():
    """
    Main function to demonstrate the circular linked list operations.
    """
    print("=== Circular Linked List Demonstration ===\n")
    
    # Create a new circular linked list
    cll = CircularLinkedList()
    
    # Test insertion operations
    print("1. Inserting nodes at the end...")
    cll.insert_end(5)
    cll.insert_end(10)
    cll.insert_end(20)
    cll.insert_end(25)
    cll.insert_end(30)
    
    print("Circular Linked List:")
    cll.display()
    print()
    
    # Test deletion
    print("2. Deleting node with value 10...")
    cll.delete_node(10)
    cll.display()
    print()
    
    # Test searching
    print("3. Searching operations...")
    print(f"Searching for 25: {cll.search(25)}")
    print(f"Searching for 100: {cll.search(100)}")
    print()
    
    # Test reversing
    print("4. Reversing the list...")
    cll.reverse()
    cll.display()
    print()
    
    # Test count nodes
    print("5. Counting nodes...")
    print(f"Total nodes: {cll.count_nodes()}")
    print()
    
    # Test clearing
    print("6. Clearing the list...")
    cll.clear()
    cll.display()
    print()
    
    # Additional tests to demonstrate more functionality
    print("=== Additional Tests ===\n")
    
    # Test insert_begin
    print("7. Testing insert_begin...")
    cll.insert_begin(100)
    cll.insert_begin(200)
    cll.insert_end(300)
    cll.display()
    print()
    
    # Test insert_after
    print("8. Testing insert_after...")
    cll.insert_after(200, 250)
    cll.insert_after(300, 350)
    cll.display()
    print()
    
    # Test edge cases
    print("9. Testing edge cases...")
    print("Trying to delete non-existent node:")
    cll.delete_node(999)
    print("Trying to insert after non-existent node:")
    cll.insert_after(999, 400)
    print()
    
    print("Final list:")
    cll.display()
    print(f"Final count: {cll.count_nodes()}")


if __name__ == "__main__":
    main()