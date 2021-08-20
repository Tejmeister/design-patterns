import copy

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.myself = self

	def __deepcopy__(self, memo):
		print(memo)
		return __class__(self.name, 90)

	def __str__(self) -> str:
		return f"{self.name} age: {self.age}"


if __name__ == "__main__":
	p = Person("Tej", 20)
	s = Person("Tejas", 21)

	t = copy.deepcopy(p)

	print(p)
	print(s)


	p.name = "Sej"

	print(p)
	print(t)
