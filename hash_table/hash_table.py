class Hashtable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.tab = [None for k in range(size)]
        self.c1 = c1
        self.c2 = c2

    def hashing(self, key):
        if type(key) is str:
            modulo_sum = 0
            for element in key:
                modulo_sum += ord(element)
            return modulo_sum % self.size

        else:
            return key % len(self.tab)

    def collision(self, key, it):
        solution = (self.hashing(key) + self.c1 * it + self.c2 * it ** 2) % self.size
        return solution

    def insert(self, key, value):
        possibility = False
        for k in range(self.size):
            hash_key = self.collision(key, k)
            if not self.tab[hash_key]:
                self.tab[hash_key] = (key, value)
                possibility = True
                break
            elif self.tab[hash_key][0] == key:
                self.tab[hash_key] = (key, value)
                possibility = True
                break
            else:
                possibility = False
        if possibility is False:
            raise Exception('Brak miejsca')

    def search(self, key):
        possibility = None
        for k in range(self.size):
            if self.tab[self.collision(key, k)]:
                if self.tab[self.collision(key, k)][0] == key:
                    possibility = self.tab[self.collision(key, k)][1]
                    break
                else:
                    possibility = None
            else:
                possibility = None

        return possibility

    def remove(self, key):
        possibility = False
        for k in range(self.size):
            hash_key = self.collision(key, k)
            if self.tab[hash_key]:
                if self.tab[hash_key][0] == key:
                    self.tab[hash_key] = None
                    possibility = True
                break
            else:
                possibility = False

        if possibility is False:
            raise Exception('Brak danej')

    def str(self):
        caption = '{  '
        for element in self.tab:
            if element:
                caption += str(element[0]) + ":" + str(element[1]) + " , "
            else:
                caption += str(None) + ", "
        caption += '}'
        print(caption)


def test1(c1, c2):
    table = Hashtable(size=13, c1=c1, c2=c2)
    try:
        table.insert(1, 'A')
        table.insert(2, 'B')
        table.insert(3, 'C')
        table.insert(4, 'D')
        table.insert(5, 'E')
        table.insert(18, 'F')
        table.insert(31, 'G')
        table.insert(8, 'H')
        table.insert(9, 'I')
        table.insert(10, 'J')
        table.insert(11, 'K')
        table.insert(12, 'L')
        table.insert(13, 'M')
    except Exception:
        print('Brak miejsca')
    table.str()
    print(table.search(5))
    print(table.search(14))
    table.insert(5, 'Z')
    print(table.search(5))
    try:
        table.remove(5)
    except Exception:
        print('Brak danej')
    table.str()
    print(table.search(31))
    table.insert('test', 'W')
    table.str()


def test2(c1, c2):
    table = Hashtable(size=13, c1=c1, c2=c2)
    try:
        table.insert(13, 'A')
        table.insert(26, 'B')
        table.insert(39, 'C')
        table.insert(52, 'D')
        table.insert(65, 'E')
        table.insert(78, 'F')
        table.insert(91, 'G')
        table.insert(104, 'H')
        table.insert(117, 'I')
        table.insert(130, 'J')
        table.insert(143, 'K')
        table.insert(156, 'L')
        table.insert(169, 'M')
    except Exception:
        print('Brak miejsca')
    table.str()


test1(1, 0)
test2(1, 0)
test2(0, 1)
test1(0, 1)
