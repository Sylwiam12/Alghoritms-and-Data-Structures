The aim of the exercise is to use a reallocated array as the "base" to create a queue. Because Python has built-in support for dynamic arrays and manages memory itself, creating an array with "manual" reallocation in it requires certain limitations to be accepted:
we implement the array as a list of a given size, for example:
tab = [None for i in range(size)]
In addition, we introduce a "prosthesis" for the realloc function:
def realloc(tab, size):
oldSize = len(tab)
return [tab[i] if i<oldSize else None for i in range(size)]

Using the above constructions, implement a circular queue.
Define a class representing the queue. The representation of the queue should contain fields storing: the array, its current size, the index of the write position to the queue, and the index of the read position from the queue.
Then, implement the following methods:

- a constructor creating an empty queue - BUT here a 5-element array (currently empty) should    be created, the size will be set to 5 and both indices to 0.
- is_empty - returning True if the read position index is equal to the write position index.
- peek - returning data from the read position or None for an empty queue.
- dequeue - returning None if the queue is empty or data from the read position (then the read position index is shifted by 1, taking into account any looping at the end of the array).
- enqueue - receiving data to be inserted into the queue, after which the write position index should be shifted by 1, taking into account any looping at the end of the array. If after shifting both indices are the same, the array should be doubled in size twice by reallocation and the data should be appropriately spread - everything from the "meeting" of the indices to the "old" end of the array must be moved to the end of the enlarged array. It is important to remember to update the array size and read position index accordingly.
For testing purposes, functions/methods that print the array (printing the standard Python list) and the queue (in the form of a Python list, i.e. a sequence of values in square brackets []) will also be useful.