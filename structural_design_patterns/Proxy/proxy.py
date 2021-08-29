from abc import ABC, abstractmethod


class Database(ABC):
	"""
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """
	@abstractmethod
	def request(self) -> None:
		pass


class OracleDatabase(Database):
	"""
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """
	def request(self) -> None:
		print("Oracle Database: Handling request.")


class ProxyOracleDatabse(Database):
	"""
    The Proxy has an interface identical to the RealSubject.
    """
	def __init__(self, real_databse: OracleDatabase) -> None:
		self._real_databse = real_databse

	def request(self) -> None:
		"""
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

		if self.check_access():
			self._real_databse.request()
			self.log_access()

	def check_access(self) -> bool:
		print("Proxy: Checking access prior to firing a real request.")
		return True

	def log_access(self) -> None:
		print("Proxy: Logging the time of request.", end="")


def client_code(database: Database) -> None:
	"""
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """

	# ...

	database.request()

	# ...


if __name__ == "__main__":
	print("Client: Executing the client code with a real database:")
	real_database_obj = OracleDatabase()
	client_code(real_database_obj)

	print("-"*60)

	print("Client: Executing the same client code with a proxy database:")
	proxy = ProxyOracleDatabse(real_database_obj)
	client_code(proxy)
