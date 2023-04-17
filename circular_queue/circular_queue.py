def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]


class Queue:
    def __init__(self, size=5):
        self.size = size
        self.tab = [None for i in range(size)]
        self.read = 0
        self.save = 0

    def is_empty(self):
        if self.save == self.read:
            return True

    def peek(self):
        if self.is_empty():
            return None
        else:
            element = self.tab[self.read]
            return element

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            currently_data = self.tab[self.read]
            self.read += 1
            if self.read == self.size:
                self.read = 0
            return currently_data

    def enqueue(self, data):
        self.tab[self.save] = data
        self.save += 1
        if self.save == self.size:
            self.save = 0
        if self.read == self.save:
            new_size = 2 * self.size
            self.tab = realloc(self.tab, new_size)
            h_size = self.read + self.size
            if new_size > h_size:
                for k in range(1, self.size):
                    self.tab[k], self.tab[k + self.size] = None, self.tab[k]
            self.read += self.size
            self.size *= 2

    def tstr(self):
        print(self.tab)

    def qstr(self):
        lst = []
        if self.is_empty():
            lst = []
        else:
            if self.save < self.read:
                for k in range(self.read, self.size):
                    lst.append(self.tab[k])
                for k in range(0, self.save + 1):
                    lst.append(self.tab[k])
            else:
                for k in range(self.read, self.save + 1):
                    lst.append(self.tab[k])

        return_lst = []
        for m in lst:
            if m:
                return_lst.append(m)
        print(return_lst)


queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)

print(queue1.dequeue())
print(queue1.peek())
queue1.qstr()
queue1.enqueue(5)
queue1.enqueue(6)
queue1.enqueue(7)
queue1.enqueue(8)
queue1.tstr()

while not queue1.is_empty():
    print(queue1.dequeue())
queue1.qstr()

