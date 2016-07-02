# coding: utf-8
"""
    >>> s = ShoppingCar()
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
    Exception: JKYN1299 ainda nao foi cadastrato no sistema.
"""
import re
from lista_tipada import ListaTipada
from shopping_d import Price, CarModel, Placa, Model


def placa_padrao(placa):
    return (re.sub("\s", "", placa)).upper()


class ShoppingCarException(Exception):
    pass


class Car(Model):
    name = CarModel()
    price = Price()
    placa = Placa()

    def __repr__(self):
        return '<%s %s>' % (self.name, self.price)


class ShoppingCar(object):
    _items = ListaTipada(Car)

    def add(self, name, price, placa):
        """
            Metodo que adiciona um novo carro ao shoppingcar.
        """
        self._items.append(Car(name=name, price=price, placa=placa))

    def __getattr__(self, name):
        """
            Método que recupera um carro do shopping.
        """
        for car in self._items:
            bplaca = placa_padrao(car.placa)
            cplaca = placa_padrao(name)
            if bplaca == cplaca:
                return car
        raise Exception('%s ainda nao foi cadastrato no sistema.' % name.upper())

    def __len__(self):
        """
            Método que recupera quantos carros existe no shoppingcar.
        """
        return len(self._items)

    @property
    def total(self):
        """
            Metodo que verifica o valor total de carros que existem no shoppingcar.
        """
        return sum(car.price for car in self._items)
