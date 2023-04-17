class Element:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linkedlst:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, element):
        first_element = Element(element)
        first_element.next = self.head
        self.head = first_element

    def is_empty(self):
        if not self.head:
            return True

    def remove(self):
        first_element = self.head
        first_element.next = self.head
        self.head = None

    def length(self):
        list_length = 0
        current_elem = self.head
        while current_elem:
            list_length += 1
            current_elem = current_elem.next
        return list_length

    def get(self):
        first_element = self.head
        return first_element.data

    def str(self):
        element = self.head
        while element:
            print(element.data)
            element = element.next

    def add_to_end(self, element):
        new_element = Element(element)
        if not self.head:
            self.head = new_element
        else:
            element = self.head
            while element.next:
                element = element.next
            element.next = new_element

    def remove_from_end(self):
        if not self.head.next:
            self.head = None
        else:
            element = self.head
            while element.next.next:
                element = element.next
            element.next = None

    def take(self, n):
        number = 0
        current = self.head
        lst = Linkedlst()
        if n > self.length():
            return self
        else:
            while number < n:
                if current:
                    lst.add_to_end(current.data)
                    number += 1
                    current = current.next
        return lst

    def drop(self, n):
        lst = Linkedlst()
        if n < self.length():
            element = self.head
            for k in range(n):
                element = element.next
            lst.add(element.data)
            for k in range(n + 1, self.length()):
                element = element.next
                lst.add_to_end(element.data)
            return lst
        return lst


element1 = Element(('AGH', 'Kraków', 1919))
element2 = Element(('UJ', 'Kraków', 1364))
element3 = Element(('PW', 'Warszawa', 1915))
element4 = Element(('UW', 'Warszawa', 1915))
element5 = Element(('UP', 'Poznań', 1919))
element6 = Element(('PG', 'Gdańsk', 1945))

lista = Linkedlst()
lista.head = element1
lista.remove()
lista.add(('AGH', 'Kraków', 1919))
lista.head.next = element2
element2.next = element3
element3.next = element4
element4.next = element5
element5.next = element6
lista.remove_from_end()
lista.add_to_end(('PG', 'Gdańsk', 1945))
lista.str()

print('długość listy:', lista.length())
print('czy lista jest pusta?', lista.is_empty())
print('pierwszy element listy to:', lista.get())
print('lista utworzona z 4 pierwszych elementów:')
lista.take(4).str()
print('lista utworzona z pominięciem 2 pierwszych elementów:')
lista.drop(2).str()
lista.destroy()