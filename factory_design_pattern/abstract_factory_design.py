"""
The Factory pattern deals with creating objects of a single type, while the Abstract Factory pattern deals with creating objects of related types
"""
from abc import ABC, abstractmethod

class ProductFactory(ABC):

	@abstractmethod
	def detail(self):
		pass

	@abstractmethod
	def price(self):
		pass


class DetailBase(ABC):

	@abstractmethod
	def show():
		pass


class PriceBase(ABC):

	@abstractmethod
	def show():
		pass


class MobileDetail(DetailBase):
	def __init__(self, mobile):
		self.mobile = mobile

	def show(self):
		return f"Mobile Detail is: {self.mobile._name}"


class MobilePrice(PriceBase):
	def __init__(self, mobile):
		self.mobile = mobile

	def show(self):
		return f"Mboile price is: {self.mobile._price}"


class GiftCardDetail(DetailBase):
	def __init__(self, gift_card):
		self.gift_card = gift_card

	def show(self):
		return f"Mobile Detail is: {self.gift_card._company}"


class GiftCardPrice(PriceBase):
	def __init__(self, gift_card):
		self.gift_card = gift_card

	def show(self):
		return f"GiftCard Price is: {self.gift_card._min_price} to {self.gift_card._max_price}"



class Mobile(ProductFactory):
	def __init__(self, name, price):
		self._name = name
		self._price = price

	@property
	def detail(self):
		return MobileDetail(self)

	@property
	def price(self):
		return MobilePrice(self)


class GiftCard(ProductFactory):
	def __init__(self, company, min_price, max_price):
		self._company = company
		self._min_price = min_price
		self._max_price = max_price

	@property
	def detail(self):
		return GiftCardDetail(self)

	@property
	def price(self):
		return GiftCardPrice(self)


if __name__ == "__main__":

	m1 = Mobile(name="g1", price=200)
	m2 = Mobile(name="g2", price=350)

	g1 = GiftCard(company="xbox", min_price=10, max_price=15)
	g2 = GiftCard(company="xbox", min_price=15, max_price=20)

	products = [m1, m2, g1, g2]

	for product in products:
		print(product.detail.show(), product.price.show())
		
