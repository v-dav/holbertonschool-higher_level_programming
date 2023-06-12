#!/usr/bin/python3
"""A module with classes for a Singly Linked List"""


class Node():
    """A class that creates a single Node in a Linked List.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        '''
         Updates the value for the data
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


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
