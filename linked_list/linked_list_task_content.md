Implement a singly linked list in Python. Let it be implemented as a class containing the head field.The head field should be understood as a pointer to the first element of the list (a separate class representing list elements should be created). This field should be set to None in the constructor (so the constructor will be equivalent to a function that creates an empty list).

Implement the following functionalities:
Transformers:
- create - this role will be performed by the constructor that creates an object representing a list with the head field set to None
- destroy - deleting/destroying the entire list - this is also easy - just set the head to None and Python will release the memory itself :)
- add - a method that adds to the beginning of the list
- remove - a method that removes an element from the beginning of the list
Observables:
- is_empty - a method that returns True for an empty list
- length - a method that counts the number of elements
- get - a method that returns the first element (only data, without a pointer - the internal representation should be hidden)

as well as methods allowing:
to print the list (it doesn't have to be str, just printing the list on the screen, assuming that the data from the list element can be printed with print)
add an element to the end of the list
remove an element from the end

Additionally, supplement the class with methods:
- take(n) - a method that creates a new linked list with the first n elements of the list (all elements are taken if n is greater than the size)
- drop(n) - a method that creates a new linked list with the elements of the given list except for its first n elements (an empty list is returned if n is greater than the size)
Note - the order of elements in the new lists should not be reversed.
