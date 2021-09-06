from order import Order
from broker import Broker
from stock import Stock
from buy_stock import BuyStock
from sell_stock import SellStock


if __name__ == "__main__":
	reliance = Stock("Reliace", 200, 2100.56)
	jswsteel = Stock("JSW Steel", 100, 1240)

	buy_reliance = BuyStock(reliance)
	buy_jsw = BuyStock(jswsteel)
	sell_reliance = SellStock(reliance)
	sell_jsw = SellStock(jswsteel)

	broker = Broker()
	broker.take_order(buy_reliance)
	broker.take_order(buy_jsw)
	broker.take_order(sell_jsw)
	broker.take_order(sell_reliance)

	broker.place_orders()

