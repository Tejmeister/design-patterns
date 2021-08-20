class SingletonMeta(type):
	"""
	The Singleton class can be implemented in different ways in Python. Some
	possible methods include: base class, decorator, metaclass. We will use the
	metaclass because it is best suited for this purpose.
	"""

	_instances = {}

	def __call__(cls, *args, **kwargs):
		"""
		Possible changes to the value of the `__init__` argument do not affect
		the returned instance.
		"""
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
	def __init__(self, name) -> None:
		self.name = name

	def some_business_logic(self):
		"""
		Finally, any singleton should define some business logic, which can be
		executed on its instance.
		"""

	def __str__(self) -> str:
		return self.name

class MotherBoard(metaclass=SingletonMeta):
	def __init__(self, name) -> None:
		self.name = name

	def some_business_logic(self):
		"""
		Finally, any singleton should define some business logic, which can be
		executed on its instance.
		"""

	def __str__(self) -> str:
		return self.name

if __name__ == "__main__":
	# The client code.

	s1 = Singleton("Tejas")
	s2 = Singleton("Parmar")



	print(s1)
	print(s2)

	if id(s1) == id(s2):
		print("Singleton works, both variables contain the same instance.")
	else:
		print("Singleton failed, variables contain different instances.")


	print(SingletonMeta._instances)

	m = MotherBoard("Intel")

	print(SingletonMeta._instances)