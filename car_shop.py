# coding: utf-8
"""
    >>> s = CarShop()
    >>> s.add('Corolla', 50000, 'LIPE 1235')
    >>> len(s)
    1
    >>> s.lipe1235
    <Corolla 50000>
    >>> s.add("Fusca", 1500, 'CARO 1238')
    >>> s.total
    51500
    >>> s.jkyn1299
    Traceback (most recent call last):
    ...
    ...
    Exception: JKYN1299 car not found.
"""
import re
from custom_list import CustomList
from model import Price, CarModel, LicensePlate, Model


def license_plate_pattern(license_plate):
    return (re.sub("\s", "", license_plate)).upper()


class ShoppingCarException(Exception):
    pass


class Car(Model):
    name = CarModel()
    price = Price()
    placa = LicensePlate()

    def __repr__(self):
        return '<%s %s>' % (self.name, self.price)


class CarShop(object):
    _items = CustomList(Car)

    def add(self, name, price, placa):
        """
            Method add a new car on the CarShop.
        """
        self._items.append(Car(name=name, price=price, placa=placa))

    def __getattr__(self, name):
        """
            Method get information about specific car.
        """
        for car in self._items:
            if license_plate_pattern(car.placa) == license_plate_pattern(name):
                return car
        raise Exception('%s car not found.' % name.upper())

    def __len__(self):
        """
            Method get the quantity of the cars in CarShop.
        """
        return len(self._items)

    @property
    def total(self):
        """
            Method get the total cost of the cars in CarShop.
        """
        return sum(car.price for car in self._items)
