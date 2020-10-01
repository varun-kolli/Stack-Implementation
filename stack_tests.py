import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.peek(), 0)

    def test_empty(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_full(self):
        stack = Stack(1)
        self.assertFalse(stack.is_full())
        stack.push(1)
        self.assertTrue(stack.is_full())

    def test_size(self):
        stack = Stack(1)
        stack.push(1)
        self.assertEqual(stack.size(), 1)

    def test_push(self):
        stack = Stack(1)
        stack.push(1)
        self.assertTrue(stack.peek(), 1)

    def test_pop(self):
        stack = Stack(2)
        stack.push(1)
        stack.push(2)
        stack.pop()
        self.assertTrue(stack.peek(), 1)

    def test_push_error(self):
        stack = Stack(1)
        stack.push(1)
        with self.assertRaises(IndexError):
            stack.push(6)

    def test_pop_error(self):
        stack = Stack(1)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_error(self):
        stack = Stack(1)
        x = stack
        with self.assertRaises(IndexError):
            stack.peek()
        self.assertEqual(x, stack)




if __name__ == '__main__': 
    unittest.main()
