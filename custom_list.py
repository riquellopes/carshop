# coding: utf-8
"""
    >>> l = CustomList(str)
    >>> l.append('henrique')
    >>> l[0]
    'henrique'
    >>> l[0] = 1
    Traceback (most recent call last):
    ...
    ...
    TypeError: That list accept only the type <str>.
    >>> l.append(10)
    Traceback (most recent call last):
    ...
    ...
    TypeError: That list accept only the type <str>.
"""


class CustomList(list):

    def __init__(self, type):
        self.type = type

    def __validation(self, value):
        if not isinstance(value, self.type):
            raise TypeError("That list accept only the type <%s>." % self.type.__name__)

    def __setitem__(self, pos, value):
        self.__validation(value)
        super(CustomList, self).__setitem__(pos, value)

    def append(self, value):
        self.__validation(value)
        super(CustomList, self).append(value)
