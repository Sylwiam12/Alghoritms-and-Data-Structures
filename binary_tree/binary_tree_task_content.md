Implement a binary search tree (BST) in Python. It should be implemented using two classes: the first class contains a "root" field that points to the root node of the tree, and the second class represents a tree node and contains four fields: key, value, and pointers to the left and right child nodes.

Implement the following functionalities:

Constructor - creates an object representing a tree with the root field set to None.
Search - searches and returns the value corresponding to the given key (or None).
Insert - inserts the given value according to the given key. If an element with the same key already exists, its value should be overwritten (the function remembers the predecessor, see lecture).
Delete - removes the element with the given key.
Print - prints the contents of the tree as a list from the smallest to the largest key in the form of key:value.
Height - a method that returns the height of the tree from the given node to the node that does not have any children (leaf node) - the longest path in the tree.
The search function performs a recursive search for an element in the tree based on the key.
The insert function creates new tree elements based on the given key. The right branch contains keys greater than the key in the parent node, and the left branch contains keys smaller than the key in the parent node.

The delete function removes a tree element based on the given key. Three cases should be considered:

Removing a node that does not have child nodes.
Removing a node with one child.
Removing a node that has two child nodes - the deleted node is replaced with the minimum key from the right subtree (successor node).