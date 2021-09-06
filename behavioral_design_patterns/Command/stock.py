class Stock:
	def __init__(self, stock_name: str, stock_quantity: int, stock_price: float) -> None:
		self.stock_name = stock_name
		self.stock_quantity = stock_quantity
		self.stock_price = stock_price

	def buy(self):
		print(f"Bought Stock: {self.stock_name}, Quantity: {self.stock_quantity}, Price:{self.stock_price} ")

	def sell(self):
		print(f"Sold Stock: {self.stock_name}, Quantity: {self.stock_quantity}, Price:{self.stock_price} ")