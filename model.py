# coding: utf-8
"""
    >>> class Car(object):
    ...     def __init__(self, name, price, placa):
    ...         self.name = name
    ...         self.price = price
    ...	        self.placa = placa
    >>> car1 = Car('Fusca', 5000, 'LLKY 1234')
    >>> car1.name
    'Fusca'
    >>> class Car(Model):
    ...     price = Price()
    ...     name = CarModel()
    ...     license_plate = LicensePlate()
    >>> car2 = Car(name='Corolla', price=5000, license_plate='LYDA 1456')
    >>> car2.name
    'Corolla'
    >>> car2.price
    5000
    >>> car2.license_plate
    'LYDA 1456'
    >>> car2.name = 'Fusca'
    >>> car2.name
    'Fusca'
    >>> car3 = Car(name='Corola', price=-5000, placa='LYDA 1456')
    Traceback (most recent call last):
    ...
    ...
    TypeError: Price can't be negative.
    >>> car4 = Car(name='Corolla', price=5000, license_plate='la1dYYo4')
    Traceback (most recent call last):
    ...
    ...
    TypeError: The license plate it's not a valid.
    >>> car5 = Car(name='Sofa', price=10, license_plate='IIUU 8712')
    Traceback (most recent call last):
    ...
    ...
    TypeError: 'Sofa' not a valid car.
"""
import re
from abc import abstractmethod, ABCMeta


class Validate(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def validation(self, instance, value):
        """
            Return value of raise TypeError for invalid values

            This method is invoked by the __set__ method of the descriptor.
            Parameters are the same for __set__: self, instance, value.
        """

    def __set__(self, instance, value):
        value = self.validation(instance, value)
        setattr(instance, '__'+self.attr_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, '__'+self.attr_name)


class Price(Validate):

    def validation(self, instance, value):
        if value < 1:
            raise TypeError("Price can't be negative.")
        return value


class CarModel(Validate):
    _carmodels = "fusca corolla chevette palio vectra punto sandeiro corsa civic".split()

    def validation(self, instance, value):
        if value.lower() not in self._carmodels:
            raise TypeError("'%s' not a valid car." % value)
        return value


class LicensePlate(Validate):

    def validation(self, instance, value):
        # Brazilian pattern
        if not re.match('\w{4}\s\d{4}', value):
            raise TypeError("The license plate it's not a valid.")
        return value


class Meta(type):

    def __new__(cls, name, bases, dict):
        for name, attr, in dict.items():
            if isinstance(attr, Validate):
                attr.attr_name = name
        return type.__new__(cls, name, bases, dict)


class Model(object):
    __metaclass__ = Meta

    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])
