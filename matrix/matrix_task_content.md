Implement a two-dimensional array (matrix) in Python, which can be accessed in a similar way as in C, i.e.:
array_name[row_number][column_number]

The implemented data type should allow addition (using the + operator) and matrix multiplication (using the * operator). Please use a class to implement this. As a reminder, the special (so-called magic) methods that define the appropriate operators are:

add - defines +
mul - defines *
getitem - defines []

Additionally, please provide the ability to print the matrix (row by row) using the print function by defining the str method (the output format is given in the example below).

The class should also have a size method that returns the number of rows and columns (ALTERNATIVELY: the len method should be implemented).

In the addition and multiplication operations, please check whether the matrices have the appropriate sizes. The result of these operations should be a new object.

The matrix itself can be represented as a list of lists, but the internal field representing the matrix (i.e. that list of lists) should not be accessible outside the class. You should implement a "constructor" that creates the matrix (an object of the class being created) in two ways:

It receives a tuple containing both dimensions of the matrix as an argument.
It receives a list of lists filled with values directly.
You can use isinstance to check if the argument is a tuple, and otherwise assume that the "constructor" received a correct list of lists. Let the "constructor" also have a default parameter (with a value of 0) used to fill the matrix with a constant value when creating a matrix by specifying its dimensions.

Write a separate function (NOT a class method, to avoid using the internal representation of the matrix) that transposes the matrix. Let this function receive a matrix and return the transposed matrix.