from typing import List


from typing import List
from order import Order

class Broker():
	_order_list : List[Order] = []

	@classmethod
	def take_order(cls, order: Order):
		cls._order_list.append(order)

	@classmethod
	def place_orders(cls):
		for order in cls._order_list:
			order.execute()
