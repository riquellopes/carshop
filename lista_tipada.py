# coding: utf-8
"""
    >>> l = ListaTipada(str)
    >>> l.append('henrique')
    >>> l[0]
    'henrique'
    >>> l[0] = 1
    Traceback (most recent call last):
    ...
    ...
    TypeError: Essa lista aceita apenas o tipo <str>.
    >>> l.append(10)
    Traceback (most recent call last):
    ...
    ...
    TypeError: Essa lista aceita apenas o tipo <str>.
"""


class ListaTipada(list):

    def __init__(self, type):
        self.type = type

    def validation(self, value):
        if not isinstance(value, self.type):
            raise TypeError("Essa lista aceita apenas o tipo <%s>." % self.type.__name__)

    def __setitem__(self, pos, value):
        self.validation(value)
        super(ListaTipada, self).__setitem__(pos, value)

    def append(self, value):
        self.validation(value)
        super(ListaTipada, self).append(value)
