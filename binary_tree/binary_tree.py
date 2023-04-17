class TreeNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class Rootnode:
    def __init__(self, root=None):
        self.root = root

    def search(self, key, node=None):
        if not self.root:
            return None
        if not node:
            node = self.root
        if node.key == key:
            return node.value
        elif node.key < key and node.right:
            return self.search(key, node.right)
        elif node.key > key and node.left:
            return self.search(key, node.left)

    def insert(self, key, value, node=None):
        if not self.root:
            self.root = TreeNode(key, value)

        if not node:
            node = self.root

        if node.key == key:
            node.value = value

        elif key > node.key:
            if not node.right:
                new_node = TreeNode(key, value)
                node.right = new_node
                new_node.parent = node
            else:
                self.insert(key, value, node.right)

        else:
            if not node.left:
                new_node = TreeNode(key, value)
                node.left = new_node
                new_node.parent = node
            else:
                self.insert(key, value, node.left)

    def delete(self, key, node=None):
        if not self.root:
            return None
        if not node:
            node = self.root
        if node.key < key:
            node.right = self.delete(key, node.right)
            return node
        elif node.key > key:
            node.left = self.delete(key, node.left)
            return node
        # 0 dzieci
        if not node.right and not node.left:
            return None
        # 1 dziecko-lewe
        if node.left and not node.right:
            return node.left
        # 1 dziecko-prawe
        if node.right and not node.left:
            return node.right
        # 2-dzieci
        if node.left and node.right:
            self.parent = node
            actual_child = node.right
            while actual_child.left:
                self.parent = actual_child
                actual_child = actual_child.left
            if self.parent == node:
                self.parent.right = actual_child.right
            else:
                self.parent.left = actual_child.right
            node.key = actual_child.key
            node.value = actual_child.value
            return node
    # nowy print
    def std_help(self, node):
        lst = []
        if node:
            if node.right:
                lst += self.std_help(node.right)
            lst.append((node.key, node.value))
            if node.left:
                lst += self.std_help(node.left)
        return lst

    def std(self):
        lst = sorted(self.std_help(self.root))
        caption = '{'
        for k in range(len(lst)):
            key, value = lst[k][0], lst[k][1]
            caption += str(key) + ": " + "'" + str(value) + "', "
        caption += '}'
        print(caption)

    def height_help(self, node=None):
        if not node:
            return 0
        right_side = self.height_help(node.right)
        left_side = self.height_help(node.left)
        maximum = max(left_side, right_side)
        return maximum + 1

    def height(self):
        return self.height_help(self.root)

    # z opisu zadania
    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self._print_tree(node.left, lvl + 5)


node = Rootnode()
node.insert(50, 'A')
node.insert(15, 'B')
node.insert(62, 'C')
node.insert(5, 'D')
node.insert(20, 'E')
node.insert(58, 'F')
node.insert(91, 'G')
node.insert(3, 'H')
node.insert(8, 'I')
node.insert(37, 'J')
node.insert(60, 'K')
node.insert(24, 'L')
node.print_tree()
node.std()
print(node.search(24))
node.insert(20, 'AA')
node.insert(6, 'M')
node.delete(62)
node.insert(59, 'N')
node.insert(100, 'P')
node.delete(8)
node.delete(15)
node.insert(55, 'R')
node.delete(50)
node.delete(5)
node.delete(24)
print(node.height())
node.std()
node.print_tree()
