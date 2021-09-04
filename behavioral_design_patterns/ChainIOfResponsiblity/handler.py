from __future__ import annotations
from abc import ABC, abstractmethod
from bank_account import BankAccount

class Handler(ABC):
	_next_handler : Handler = None

	def pass_request(self, handler: Handler) -> Handler:
		self._next_handler = handler
		return handler

	@abstractmethod
	def withdraw(self, account: BankAccount) -> BankAccount:
		pass