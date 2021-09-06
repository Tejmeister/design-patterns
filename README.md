# design-patterns

# Introduction

This Repository contains sample code which I developed while learning SOLID Principles and Design Patterns

# Images Source

All Images source is https://refactoring.guru/

## Build Pattern

1. Some objects are simple while some are not
2. Hence these complex objects are difficult to be intialized in a single call
3. Having an initializer with 10 arguments is not a good way
4. Hence we can opt for 'piecewise construction'
5. Builder provides an API for constructing the object step-by-step

![](images/creational_design_patterns/builder.PNG)

## Factory Pattern

1. Outsourcing the creation of object
2. Different from Builder as it is not piecewise but wholesale
3. Can create hierarchies of type (Abstract Factory)

![](images/creational_design_patterns/factory.PNG)

## Prototype Pattern

1. Complicated objects (eg. cars) are not created from scratch each time. We have an existing design and have a prototype first and then we just clone or copy the prototype
2. This helps to create objects without knowing in details the components of the class
3. A prototype is a partially or fully initialized object that you copy (clone) and make use of it

![](images/creational_design_patterns/prototype.PNG)

## Singleton Pattern

1. Lets you ensure that a class has only one instance, while providing a global access point to this instance.
2. Used when a single instance is required of some class throughout the project.
3. For example, you may want only a single connection object to the database and every class can use the same object

![](images/creational_design_patterns/singleton.PNG)

## Adapter Pattern

1. A construct which adapts an existing interface X to conform to the required interface Y
2. It allows objects with incompatible interfaces to collaborate

![](images/structural_design_patterns/adapter.PNG)

## Bridge Pattern

1. Prevents 'cartesion product' complexity explosion
   a. 2 shapes and 2 colors (2X2). Add another shape and combinations become (3X2)
2. A mechanism that decouples an interface from an implementation
3. Difficult to maintain a huge monolith
4. Hence split into smaller components for easier maintainability

![](images/structural_design_patterns/bridge1.PNG)

![](images/structural_design_patterns/bridge2.PNG)

## Composite Pattern

1. Lets you compose objects into tree structures and work with these objects as if they are individual objects
2. Basically lets you make compound objects
3. Objects use the objects' properties through inheritance and composition
4. Use the pattern when you want the client code to treat both simple and complex elements uniformly.

![](images/structural_design_patterns/composite.JPG)


## Flyweight Pattern

1. Lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object
2. eg. git. Git saves a single blob file across multiple branche unless and until there is any change to that file

![](images/structural_design_patterns/flyweight.PNG)


## Proxy Pattern

1. Lets you provide a substitute for another object. A proxy controls the access to the original object allowing you to perform something either before or after the request goes to the original object
2. Proxy and Original class should provide the same interface to the client

![](images/structural_design_patterns/proxy1.PNG)

![](images/structural_design_patterns/proxy2.PNG)


## Facade Pattern
1. Provides a simplified (maybe limited) interface to a complex set of classes, library or framework.
2. Example, starting a computer. You need to only press the start button and the computer does a series of steps internally
Here the start button is a facade

![](images/structural_design_patterns/facade.PNG)

## Decorator Pattern
1. lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors
2. Eg. Counter Strike. you have Player baseclass and Counter Terrorist and Terrorist. They can be decorated with behaviours like using different weapons. Different weapons can be bought with different money and hence is known at runtime

## Chain of Responsibilty Pattern
1. lets you pass requests along a chain of handlers
2. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain

![](images/behavioral_design_patterns/chainofresponsibility.PNG)


## Command Pattern
1. turns a request into a stand-alone object that contains all information about the request. 
2. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

