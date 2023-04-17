Implement a hash table as a class containing a 'static array', for example:
tab = [None for i in range(size)]
where size is a constructor parameter.

The class should have implemented a method performing a hashing function, calculating modulo the size of the array, and a method solving collisions using open addressing (with quadratic probing, where c1 and c2 should be constructor parameters with default settings of 1 and 0 - so we have linear sampling by default). We assume that the hashing function can receive a number or a string - in the latter case, it should be converted to a number by summing the ASCII codes of all its letters (using the ord function).

Then you should implement the following methods:
- constructor (with parameters: the size of the array and c1, c2 as above) creating an empty array (filled with None)
search - searching for and returning the value corresponding to the given key (or None if not found)
- insert - inserting data according to the given key, if an element with such a key already exists, its value should be overwritten
- remove - removing data with the given key (initially, implement removal by writing None in the place indicated by the calculated index).
- str - printing the array in the form of pairs {key:value, ...} - just like a Python dictionary is printed; 'Empty' place should be printed as None
The insert and remove methods should somehow inform about failure (insert - no space, remove - no data with the given key). It can be for example an exception or a returned value of None. In such a case, the messages "No space" and "No data" should appear at the calling site.

The elements of the array should also be implemented as a class with two attributes storing: the key and the value (some data).