class Element:
    def __init__(self,priority=None,data=None):
        self.data=data
        self.priority=priority

    def std(self):
        return str(self.priority)+":"+str(self.data)
    
    def __lt__(self,new):
        return bool(self.priority<new.priority)

    def __gt__(self,new):
        return bool(self.priority>new.priority)

    
class Queue:
    def __init__(self,capacity=8):
        self.size=0
        self.tab=[Element() for i in range(capacity)]
        self.capacity=capacity

    def is_empty(self):
        if not self.tab:
            return True

    def parent(self,index):
        return (index-1)//2

    def left(self,index):
        return 2*index+1
    
    def right(self,index):
        return 2*index+2

    def left_exists(self,index):
        return self.left(index)<self.size
        
    def right_exists(self,index):
        return self.right(index)<self.size

    def peek(self):
        return self.tab[0].data

    def enqueue(self,priority,data):
        if not self.size==self.capacity:
            self.tab[self.size]=Element(priority,data)
            actual_size=self.size
            while actual_size > 0 and (self.tab[self.parent(actual_size)] < self.tab[actual_size]):
                self.tab[self.parent(actual_size)],self.tab[actual_size]=self.tab[actual_size],self.tab[self.parent(actual_size)]
                actual_size = self.parent(actual_size)
            self.size+=1
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            maxp_element=self.tab[0]
            self.tab[0],self.tab[self.size-1]=self.tab[self.size-1],self.tab[0]
            self.tab.pop(self.size-1)
            self.size-=1
            self.heapify() 
        return maxp_element.data

    def heapify(self,index=0):
        change_place=index
        if self.left_exists(index):
            actual_left=self.left(index)
            if self.tab[actual_left] > self.tab[index]:
                change_place=actual_left
        if self.right_exists(index):
            actual_right=self.right(index)
            if self.tab[actual_right] > self.tab[change_place]:
                change_place=actual_right
        if index != change_place:
            self.tab[index], self.tab[change_place] = self.tab[change_place], self.tab[index]
            self.heapify(change_place)


    def print_tab(self):
        caption='{'
        if self.size==0:
            caption+='}'
        else:
            for i in range(self.size):
                caption+=str(self.tab[i].std())+', '
            caption+='}'
        print(caption)

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx].std() if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)

new=Queue()
keys=[4,7,6,7,5,2,2,1]
values=['A','L','G','O','R','Y','T','M']
for element in range(len(keys)):
    new.enqueue(keys[element],values[element])
new.print_tree(0,0)
new.print_tab()
print(new.dequeue())
print(new.peek())
new.print_tab()
while new.size>0:
    print(new.dequeue())
new.print_tab()