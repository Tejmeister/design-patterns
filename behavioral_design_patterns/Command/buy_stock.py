from order import Order
from stock import Stock


class BuyStock(Order):
	def __init__(self, stock: Stock):
		self._stock = stock

	def execute(self):
		self._stock.buy()