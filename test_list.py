import unittest
import linked_list

class TestList(unittest.TestCase):

    def test_pushfront(self):
        a = linked_list.LinkedList()
        a.push_front(3)
        self.assertEqual(a.head.value, 3)
        a.push_front(4)
        self.assertEqual(a.head.value, 4)
        

    def test_append(self):
        a = linked_list.LinkedList()
        a.append(5)
        self.assertEqual(a.head.value, 5)
        a.append(4)
        self.assertEqual(a.head.value, 5)
        self.assertEqual(a.size, 2)

    def test_length(self):
        a = linked_list.LinkedList()
        a.append(1)
        a.append(2)
        a.append(3)
        a.append(4)
        a.append(5)
        self.assertEqual(a.length(), 5)
        a.push_front(0)
        self.assertEqual(a.length(), 6)

    def test_clear(self):
        a = linked_list.LinkedList()
        a.append(1)
        a.append(2)
        a.append(3)
        a.append(4)
        a.append(5)

        a.clear()
        self.assertEqual(a.size, 0, "testing clear")
        self.assertEqual(a.head.get_value(), None)
        self.assertEqual(a.head.get_next(), None)
        


if __name__ == "__main__":
    unittest.main()
