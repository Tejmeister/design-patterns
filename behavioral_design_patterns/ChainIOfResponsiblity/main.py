from bank_account import BankAccount
from five_thousand_handler import FiveThousandHandler
from two_thousand_handler import TwoThousandHandler
from five_hundred_handler import FiveHundredHandler
from two_hundred_handler import TwoHundredHandler
from one_hundred_handler import OneHundredHandler

if __name__ == "__main__":
	five_thousand_handler = FiveThousandHandler()
	two_thousand_handler = TwoThousandHandler()
	five_hundred_handler = FiveHundredHandler()
	two_hundred_handler = TwoHundredHandler()
	one_hundred_handler = OneHundredHandler()

	# create chain
	five_thousand_handler.pass_request(two_thousand_handler).pass_request(five_hundred_handler).pass_request(two_hundred_handler).pass_request(one_hundred_handler)

	tejas = BankAccount(123, 20300)
	five_thousand_handler.withdraw(tejas)

