
class Node():
    # constructor
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

# A Linked List class with a single head node
class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    # print the contents of the list
    def print(self) -> None:
        pass

    # push to the front of the list
    def push_front(self, val):
        # check to see if list is empty
        if self.size == 0:
            self.head = Node(val)
        else:
            n = Node(val)
            n.next = self.head
            self.head = n
        self.size += 1
        pass        

    # append to the end of the list
    def append(self, val):
        curr = self.head
        if curr:
            while curr.get_next() != None:
                curr = curr.get_next()
            curr.set_next(Node(val))
        else:
            self.head = Node(val)

        self.size += 1

        pass

    # return the size of the list
    def length(self) -> int:
            return self.size

    # empty out the list
    def clear(self) -> None:
        curr = Node()
        prev = Node()
        curr = self.head
        prev = curr
        while curr != None:
            # move curr to the next node
            curr = curr.get_next()
            
            # reset the prev node
            prev.set_value(None)
            prev.set_next(None)

            # move prev to next node
            prev = curr

            # decrement size by 1
            self.size -= 1

        # reset head node
        self.head.set_next(None)
        self.head.set_value(None)

    # delete element i of the list
    def remove(self, index) -> None:
        # edge case: if index = 0, remove head
        if index == 0:
            curr = self.head.get_next()
            self.head.set_next(None)
            self.head.set_value(None)
        else: # otherwise, we have to go through the list
            # make current node at head
            curr = self.head
            prev = None

            # loop through the list to get to index i
            for i in range(index):
                prev = curr                 # set the prev node
                curr = curr.get_next()      # move the current node along

            prev.set_next(curr.get_next())
            curr.set_next(None)
            curr.set_value(None)

        self.size -= 1

        pass

    # get element at index i
    def get_element(self, index):
        if index == 0:
            return self.head.get_value()
        else:
            curr = self.head
            for i in range(index):
                curr = curr.get_next()
            return curr.get_value()

    # insert element into position at index i
    def insert(self, value, index) -> None:
        pass

    # replace element at position i of the list
    def replace(self, value, index) -> None:
        pass



