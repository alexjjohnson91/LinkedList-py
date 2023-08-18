
class Node():
    # constructor
    def __init__(self, value = None):
        self.value = value
        self.next = None

# A Linked List class with a single head node
class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    # print the contents of the list
    def print(self) -> None:
        pass

    # push to the front of the list
    def push_front(self, val) -> None:
        # check to see if list is empty
        # if self.size == 0:
        #     self.head = Node(val)
        # else:
        #     n = Node(val)
        #     n.next = self.head
        #     self.head = n
        # self.size += 1
        pass        

    # append to the end of the list
    def append(self, val) -> None:
        # create the new node with the value
        n = Node(val)

        # if the list is empty, then append n as head
        if self.size == 0:
            self.head = n
        else:
            # current node is equal to the head
            curr = self.head
            # loop through the list to get to the last node
            for i in range(0, self.size):
                curr = curr.next
            # now set the curr.next to the new node
            curr.next = n

        # increment size of list
        self.size += 1

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



