#!/usr/bin/python3
"""A module with a locked class"""


class LockedClass:
    """A class that with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """

    __slots__ = ["first_name"]
    """`__slots__ = ["first_name"]` is defining a special class attribute that
    restricts the creation of instance attributes to only those listed
    in the `__slots__` list. In this case, the `LockedClass` can only have an
    instance attribute called `first_name`. Any attempt to create a
    new instance attribute with a different name will result in
    an `AttributeError`. This is a way to optimize memory usage
    and prevent accidental creation of new instance attributes.
    """
