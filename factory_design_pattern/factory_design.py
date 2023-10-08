"""
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

"""

from abc import ABC, abstractmethod


class Animal(ABC):

	@abstractmethod
	def sound(self):
		pass


class Lion(Animal):

	def sound(self):
		return "GHRRRRRRRRR"


class Snake(Animal):

	def sound(self):
		return "sssssss!"



if __name__ == "__main__":

	lion = Lion()
	snake = Snake()

	print(lion.sound())
	print(snake.sound())
