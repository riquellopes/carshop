# coding: utf-8
"""
	O sistema ShoppingCar precisa que algumas regras sejam respeitas::
		1 - Quando o carro for cadastrado a quantidade informada nao pode < 1::
		2 - O valor de um carro nao pode ser negativo::
		3 - Nao podem haver placas repetidas::

	>>> class Car(object):
	...		def __init__(self, name, price, placa):
	...			self.name = name
	...			self.price = price
	...			self.placa = placa
	>>> car = Car('Fusca', 5000, 'LLKY 1234')
	>>> car.name
	'Fusca'
	>>> class Car(Model):
	...		price = Price()
	...		name = CarModel()
	... 		placa = Placa()
	>>> car = Car(name='Corola', price=-5000, placa='LYDA 1456')
	Traceback (most recent call last):
	...
	...
	TypeError: O preco nao pode ser negativo.
	>>> car.placa = 'la1dYYo4'
	Traceback (most recent call last):
	...
	...
	TypeError: A placa informada nao segue o padrao Brasileiro.
"""
from abc import abstractmethod, ABCMeta
import re

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
			raise TypeError('O preco nao pode ser negativo.')
		return value

class CarModel(Validate):

	def validation(self, instance, value):
		return value

class Placa(Validate):

	def validation(self, instance, value):
		if not re.match('\w{3}-\d{4}', value):
			raise TypeError( "A placa informada nao segue o padrao Brasileiro" )
		return value
		
class ModelMeta(type):

	def __new__(cls, name, bases, dict):
		for name, attr, in dict.items():
			if isinstance(attr, Validate):
				attr.attr_name = name
		return type.__new__(cls, name, bases, dict)

class Model(object):
	__metaclass__ = ModelMeta

	def __init__(self, **kwargs):
		for k in kwargs:
			setattr(self, k, kwargs[k])
