class BankAccount:
	_total_amount : int = 0
	_remaining_amount_to_issue_notes: int = 0

	def __init__(self, account_number: int, requested_amount: int) -> None:
		self.account_number = account_number
		self.requested_amount = requested_amount
		self._remaining_amount_to_issue_notes = requested_amount

	@property
	def total_amount(self):
		return self._total_amount

	@property
	def remaining_amount_to_issue_notes(self):
		return self._remaining_amount_to_issue_notes

	def get_remaining_amount_to_issue_notes(self):
		return self._remaining_amount_to_issue_notes

	def remaining_amount_to_issue_notes(self, remaining_amount_to_issue_notes):
		self._remaining_amount_to_issue_notes = remaining_amount_to_issue_notes