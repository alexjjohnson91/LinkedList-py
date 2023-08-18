
class Node():
    # constructor
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

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
        self.head = Node()
        self.size = 0

    # print the contents of the list
    def print(self) -> None:
        pass

    # push to the front of the list
    def push_front(self, val) -> None:
        # check to see if list is empty
        if self.size == 0:
            self.head.value = val
        else:
            n = Node(val)
            n.next = self.head
            self.head = n
        self.size += 1
        pass

    # append to the end of the list
    def append(self, val) -> None:
        pass

    # return the size of the list
    def length(self) -> None:
        pass

    # empty out the list
    def clear(self) -> None:
        pass

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


