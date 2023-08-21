
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
        pass

    # get element at index i
    def get_element(self, index) -> None:
        pass

    # insert element into position at index i
    def insert(self, index) -> None:
        pass

    # replace element at position i of the list
    def replace(self, index) -> None:
        pass



