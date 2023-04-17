The goal of the exercise is to implement a priority queue as a (maximum) heap implemented in the form of an array. The Python list can be used as an array (either with native support or manually reallocated, as in the exercise with a circular array).

The elements of the queue should be objects of a class whose attributes are data and priority. This class should have defined "magic" methods allowing the use of the < and > operators on its objects and printing them with the print function in the form priority: data.

The class representing the queue should contain fields storing: the array and its current size (in an implementation using the standard Python list, this field does not need to appear), and the following methods:

A constructor creating an empty queue
- is_empty - returning True if the queue is empty
peek - returning the data with the highest priority (i.e., the largest value of the priority attribute)
- dequeue - returning None if the queue is empty or the data with the highest priority (removing it from the top of the heap)
- enqueue - receiving data to be inserted into the queue (heap) along with their priority.
Additionally, to facilitate movement around the heap, please write the methods left and right, which, given the index of a node, return the index of its left and right child, respectively, and a parent method, which, based on the index of a node, returns the index of its parent.

You should also create functions/methods: one for printing the queue as a dictionary (the elements of the array as priority:data pairs separated by commas, enclosed in curly braces {}) and one for printing the queue as a tree.