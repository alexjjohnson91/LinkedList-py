import unittest
import linked_list

class TestList(unittest.TestCase):

    def setUp(self):
        """ 
            Set up the test fixtures
        """
        self.a = linked_list.LinkedList()
        self.a.append(1)
        self.a.append(2)
        self.a.append(3)
        self.a.append(4)
        self.a.append(5)
    
    def tearDown(self):
        """
            reset the self list between tests
        """
        self.a.clear()

    def test_pushfront(self):
        self.a.push_front(3)
        self.assertEqual(self.a.head.value, 3)
        self.a.push_front(4)
        self.assertEqual(self.a.head.value, 4)
        

    def test_append(self):
        self.a.append(6)
        self.assertEqual(self.a.size, 6)
        self.a.append(7)
        self.assertEqual(self.a.size, 7)


    def test_length(self):
        self.assertEqual(self.a.length(), 5)
        self.a.push_front(0)
        self.assertEqual(self.a.length(), 6)

    def test_clear(self):
        self.a.clear()
        self.assertEqual(self.a.size, 0, "testing clear")
        self.assertEqual(self.a.head.get_value(), None)
        self.assertEqual(self.a.head.get_next(), None)
        


if __name__ == "__main__":
    unittest.main()
