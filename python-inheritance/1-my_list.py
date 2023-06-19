#!/usr/bin/python3
"""A module with a class list"""


class MyList(list):
    """A class list that inherits from list"""

    def print_sorted(self):
        """A public instance method that prints the list
        in sorted ascending order

        Args: nothing

        Returns: nothing
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
