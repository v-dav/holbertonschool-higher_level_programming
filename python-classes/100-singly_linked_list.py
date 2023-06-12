#!/usr/bin/python3
"""A module with classes for a Singly Linked List"""


class Node:
    """A class that defines a node for the list"""
    def __init__(self, data, next_Node=None):
        """"Constructor function initializing a node with data and next node

        Args:
            data (int): the data to store in the node
            next_Node (Node, optional): the next node of the given node.
            Defaults to None.

        Raises:
            TypeError: If the data attribute is not an integer or the next node
                is not an object of class Node
        """
        self.__data = data
        self.next_Node = next_Node
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_Node is not None and type(next_Node) is not Node:
            raise TypeError("next node must be a Node object")

    @property
    def data(self):
        """Gets or sets the data in the node.

        When setting data, the value it must be an integer

        Raises:
            TypeError: If the data attribute is not an integer
        """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Gets or sets the next node of the node.

        When setting the next node, the value it must be an object
        of class Node.

        Raises:
            TypeError: If the next node is not an object of class Node
        """
        return self.__next_Node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next node must be a Node object")
        else:
            self.__next_Node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""
    def __init__(self):
        """Constructor function initializing a list with
        private instance attribute head pointing to none
        """
        self.__head = None

    def __str__(self):
        """This method is for string representation of the linked list.

        Returns: a string representation of the linked list. It
        concatenates the string representation of each node's data,
        separated by newline characters, and returns the resulting string.
        """
        list_str = ""
        current = self.__head
        while current:
            list_str += str(current.data)
            if current.next_node:
                list_str += "\n"
            current = current.next_node
        return list_str

    def sorted_insert(self, value):
        """
        This method inserts a new node with a given value into
        a sorted linked list.

        Args:
            value (int): The value to be inserted into the linked list
            in sorted order

        Returns: Nothing is being returned explicitly in this code.
            However, if the method is called successfully, it will modify
            the linked list by inserting a new node with the
            given value in a sorted manner.
        """
        node = Node(value)
        if self.__head is None:
            self.__head = node
            return
        if self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            curr = self.__head
            while curr.next_node is not None and curr.next_node.data < value:
                curr = curr.next_node
            node.next_node = curr.next_node
            curr.next_node = node
