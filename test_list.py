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


if __name__ == "__main__":
    unittest.main()
