from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# This is ok if you want a multifucntion printer which can print, scan and fax
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


# But problematic for old fashioned one as it may not be able to fax or scan
# But the client can still see fax and scan methods in the API
# Hence it violates the ISP
# Makes sense to segregate the interfaces into separate functionality
class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


# ------------------------------------------------------------------------------------------------------- #

# Separate Printer class to provide ability to print
class Printer:
    @abstractmethod
    def print(self, document): pass


# Separate Scanner class to provide ability to scan
class Scanner:
    @abstractmethod
    def scan(self, document): pass


# same for Fax, etc.

class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful


class MultiFunctionDevice(Printer, Scanner):  # , Fax, etc
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # oops!
