# SOLID Principles:

## Single Responsibility Principle (SRP)
1. Also known as separation of concerns
2. A class should have single responsibilty
3. Eg. A journal class and a diary class should not have their independent persistence functions in their class if they basically
do the same operation
The persistence methods can be moved to a separate class say PersistenceManager so that you can edit the method if required at one
central level

## Open-Closed Principle (OCP)
1. Open for extension, closed for modification
2. Once Classes are defined at design time there should not be modifications done in them at later point
If needed extend the base classes and create more concrete classes

The old type of implementation (a separate method for each filter type) can cause 'State Space Explosion'
For example,
we have 2 criteria, then then are at least 3 methods needed to filter properly
if we have 3 criteria, then minimum methods with only 'and' operation will be 7
c s w -> c s w cs cw sw csw

## Liskov Substitution Principle (LSP)
1. The objects of a superclass shall be replaceable with objects of its subclasses without breaking the application
which means the objects of the subclasses should behave in the same way as the objects of the superclass

## Interface Segregation Principle (ISP)
1. interface-segregation principle (ISP) states that no client should be forced to depend on methods it does not use. 
ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy
closely related to YAGNI : You aint going to need it

## Dependency Inversion Principle
1. high level classes should not depend directly on low level modules or classes, they should dependent on abstraction and not
implementation