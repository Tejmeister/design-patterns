from handler import Handler
from bank_account import BankAccount

class OneHundredHandler(Handler):
	def withdraw(self, account: BankAccount) -> BankAccount:
		requested_amount = account.get_remaining_amount_to_issue_notes()

		number_of_notes_to_be_issued = int(requested_amount / 100)
		if number_of_notes_to_be_issued > 0:
			if number_of_notes_to_be_issued > 1:
				print(number_of_notes_to_be_issued,"OneHundred notes are Issued by OneHundredHandler")
			else:
				print(number_of_notes_to_be_issued,"OneHundred note is Issued by OneHundredHandler")

		pending_amount_to_be_processed = requested_amount % 100

		if pending_amount_to_be_processed > 0:
			account.remaining_amount_to_issue_notes(pending_amount_to_be_processed)
			self._next_handler.withdraw(account)

		return account