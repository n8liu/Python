""" Linked List and Double Linked List Implementation File

contains:
Class for Linked List,
iterate, insert and remove methods for Linked List

Class for Doubly Linked List,
iterate, insert and remove methods for doubly linked list
"""

class Node:
    """ Node Class:
    methods:
    __init__: used for both singly and doubly linked lists
    __repr__: print(Node("a")) prints a

    examples:
    declare a node:
    >>> Node("a")
    a

    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data

class LinkedList:
    """ Singly Linked List Class:

    examples:
    initialization: (must take a list or string)
    >>> linked_list = LinkedList(["a","b","c"])
    >>> linked_list
    a -> b -> c -> None

    remove a node:
    >>> linked_list.remove("c")
    >>> linked_list
    a -> b -> None

    iterate through a singly linked list
    >>> for elem in linked_list: 
    ...     if elem.data == "b":
    ...         linked_list.add_after("b", Node("d"))
    ...
    >>> linked_list
    a -> b -> d -> None

    """
    def __init__(self, nodes=None):
        self.first = None
        if nodes is not None:
            node = Node(data=nodes[0])
            self.first = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def __repr__(self):
        node = self.first
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes[1:])

    def __iter__(self):
        node = self.first
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.first
        self.first = node

    def add_last(self, node):
        if not self.first:
            self.first = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def add_after(self, target_node_data, new_node):
        if not self.first:
            raise Exception("linked list is empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove(self, target_node_data):
        if not self.first:
            raise Exception("linked list is empty")

        if self.first.data == target_node_data:
            self.first = self.first.next
            return

        previous_node = self.first
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

class DoublyLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            previous_node = Node(data=nodes.pop(0))
            self.head = previous_node
            for elem in nodes:
                next_node = Node(data=elem)
                previous_node.next = next_node
                next_node.previous = previous_node
                previous_node = next_node

    def __repr__(self):
        node = self.head
        nodes = ['Doubly Linked List:']
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " <-> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("linked list is empty")
            
        for node in self:
            if node.data == target_node_data:
                node.next.previous = new_node
                new_node.next = node.next
                node.next = new_node
                new_node.previous = node
                return
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def remove(self, target_node_data):
        if not self.head:
            raise Exception("linked list is empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        for node in self:
            if node.data == target_node_data:
                node.previous.next = node.next
                if node.next != None:
                    node.next.previous = node.previous
                return

        raise Exception("Node with data '%s' not found" % target_node_data)
"""
Or you can just use collections.deque, which is a doubly linked list
"""