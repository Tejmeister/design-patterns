from __future__ import annotations
from abc import ABC, abstractmethod

class Order(ABC):
	@abstractmethod
	def execute(self) -> None:
		pass